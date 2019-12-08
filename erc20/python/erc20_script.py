from erc20 import SimpleERC20, DbERC20
import argparse


def print_tx(transfers):
    # SimpleERC20 stores transfer events as dict of {tx_id: {from: , to: , value:}}
    for i in transfers:
        this_transfer = transfers[i]
        print('Transfer {}: {}->{}  {}'.format(
            i + 1,
            this_transfer['from'], this_transfer['to'], this_transfer['value']))


def print_state(token):
    balance0 = token.balanceOf(0)
    balance1 = token.balanceOf(1)
    balance2 = token.balanceOf(2)
    if token.count_transfer > 0:
        print_tx(token.transfers)
    print(f'Account 0: {balance0}  Account 1: {balance1}  Account2: {balance2}')
    print('Total supply: {}'.format(token.totalSupply()))
    print('')


def simulation(token_ctor):
    token = token_ctor(100000)
    print_state(token)
    token.transfer(1, 1000, 0)
    print_state(token)
    token.transfer(2, 2000, 1)
    print_state(token)
    token.transfer(2, 500, 1)
    print_state(token)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='ERC20 token demo using non-blockchain backend')
    parser.add_argument('-b', dest='backend', default='db',
                        help='backend: simple, db.  Default: db')
    args = parser.parse_args()
    print('Backend: ' + args.backend)
    backends = {'simple': SimpleERC20, 'db': DbERC20}
    simulation(backends[args.backend])
