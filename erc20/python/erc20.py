import abc  # Abstract Base Class
from eth_account import Account
from collections import defaultdict
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func

Base = declarative_base()


class IERC20(abc.ABC):
    @abc.abstractmethod
    def totalSupply(self):
        pass

    @abc.abstractmethod
    def balanceOf(self, address):
        pass

    @abc.abstractmethod
    def transfer(self, address_to, value, address_from):
        # In Web3 interface we sign the transaction from address_from
        # For simplicity here just add as extra argument
        pass

    # @abc.abstractmethod
    # def approve(self, address_spender, value, address_from):
    #     pass
    #
    # @abc.abstractmethod
    # def allowance(self, address_owner, address_spender):
    #     pass
    #
    # @abc.abstractmethod
    # def transferFrom(self, address_from, address_to, value):
    #     pass


class SimpleERC20(IERC20):
    def __init__(self, supply):
        self.balance = defaultdict(int)
        self.allowance = defaultdict(int)
        self.transfers = {}
        self.approvals = {}
        self.total_supply = supply
        # Start with all funds in account 0
        self.balance[0] = supply

    def totalSupply(self):
        return self.total_supply

    def balanceOf(self, address):
        return self.balance[address]

    def transfer(self, address_to, value, address_from):
        try:
            assert value >= 0, ValueError('Can only transfer positive values')
            assert self.balance[address_from] >= value, ValueError('Insufficient funds')
            self.balance[address_from] -= value
            self.balance[address_to] += value
            self.transfers[len(self.transfers) + 1] = {
                'from': address_from,
                'to': address_to,
                'value': value
            }
            return True
        except AssertionError as ex:
            print(ex)
            return False

    @property
    def count_transfer(self):
        return len(self.transfers)


# Database backed ERC20 contract
class Balance(Base):
    __tablename__ = 'balance'
    account = Column(Integer, primary_key=True)
    value = Column(Integer)


class Transfer(Base):
    __tablename__ = 'transfer'
    tx_id = Column(Integer, primary_key=True)
    address_from = Column(Integer)
    address_to = Column(Integer)
    value = Column(Integer)


class DbERC20(IERC20):
    def __init__(self, supply):
        self.engine = create_engine('sqlite:///:memory:', echo=False)
        _session = sessionmaker(bind=self.engine)
        self.session = _session()
        Base.metadata.create_all(self.engine)
        self.session.add(Balance(account=0, value=supply))
        self.session.commit()

    def totalSupply(self):
        return self.session.query(func.sum(Balance.value)).scalar()

    def balanceOf(self, address):
        account = self.session.query(Balance.value).filter_by(account=address).first()
        return 0 if account is None else account.value

    def transfer(self, address_to, value, address_from):
        try:
            _address_from = self.session.query(Balance).filter_by(account=address_from).first()
            _address_to = self.session.query(Balance).filter_by(account=address_to).first()
            assert value >= 0, ValueError('Can only transfer positive values')
            assert _address_from.value >= value, ValueError('Insufficient funds')
            _address_from.value -= value
            if _address_to is not None:
                _address_to.value += value
            else:
                self.session.add(Balance(account=address_to, value=value))
            self.session.add(
                Transfer(tx_id=self.count_transfer, address_from=address_from,
                         address_to=address_to, value=value)
            )
            self.session.commit()
            return True
        except AssertionError as ex:
            print(ex)
            return False

    @property
    def transfers(self):
        res = {}
        for tx in self.session.query(Transfer).order_by(Transfer.tx_id):
            res[tx.tx_id] = {
                'from': tx.address_from,
                'to': tx.address_to,
                'value': tx.value
            }
        return res

    @property
    def count_transfer(self):
        return self.session.query(Transfer.tx_id).count()
