from erc20 import SimpleERC20


def print_state(token):
    balance0 = token.balanceOf(0)
    balance1 = token.balanceOf(1)
    balance2 = token.balanceOf(2)
    if len(token.transfers) > 0:
        for i in range(len(token.transfers)):
            this_transfer = token.transfers[i+1]
            print('Transfer {}: {}->{}  {}'.format(
                i+1,
                this_transfer['from'], this_transfer['to'], this_transfer['value']))
    print(f'Account 0: {balance0}  Account 1: {balance1}  Account2: {balance2}')
    print('')


def simulation():
    token = SimpleERC20(100000)
    print_state(token)
    token.transfer(1, 1000, 0)
    print_state(token)
    token.transfer(2, 2000, 1)
    print_state(token)
    token.transfer(2, 500, 1)
    print_state(token)


if __name__ == '__main__':
    simulation()
