const ERC20 = artifacts.require('ERC20');

contract("ERC20", accounts => {
    it('... should deploy and allocate all funds to accounts[0]', async () => {
        const erc20 = await ERC20.deployed();

        let startingBalance = await erc20.balanceOf(accounts[0]);

        assert.equal(startingBalance.toString(), '1000000000' + '0'.repeat(18))
    })
});