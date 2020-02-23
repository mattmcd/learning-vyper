# Coin Flip 
[Ethernaut](https://solidity-05.ethernaut.openzeppelin.com/) Coin Flip task. 
Guess correctly 10 coin flips in a row by writing an exploit contract that predicts
the result.

## Setup
Check that [Truffle](https://www.trufflesuite.com/truffle) has already been installed.

From shell:
* `truffle init` to set up directory structure 
* `npm install openzeppelin-solidity` to get the OpenZeppelin libraries

Copy `CoinFlip.sol` from Ethernaut website to contracts directory.

Create simple [migration](https://www.trufflesuite.com/docs/truffle/getting-started/running-migrations) for CoinFlip

    const CoinFlip = artifacts.require("CoinFlip");

    module.exports = function(deployer){
        deployer.deploy(CoinFlip);
    };
    
Use `truffle develop` to interact with the contract

    truffle(develop)> compile
    truffle(develop)> deploy
    truffle(develop)> let accounts = await web3.eth.getAccounts()
    truffle(develop)> let instance = await CoinFlip.deployed()
    truffle(develop)> await instance.consecutiveWins()
    truffle(develop)> await instance.flip(true, {from: accounts[0]})


    
    