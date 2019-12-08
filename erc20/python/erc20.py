import abc  # Abstract Base Class
from eth_account import Account
from collections import defaultdict


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
