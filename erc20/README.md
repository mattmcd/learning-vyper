# ERC20
The Ethereum ERC20 token standard is a way of representing fungible assets.
It has six methods that must be implemented, one for checking total supply of
tokens in existence:
* `totalSupply() public view returns (uint256)`

two for managing balance on an account and the owner transferring tokens
from the account: 
* `balanceOf(address _owner) public view returns (uint256 balance)`
* `transfer(address _to, uint256 _value) public returns (bool success)`

and three for delegated transfer of tokens from an account
* `approve(address _spender, uint256 _value) public retuns (bool success)`
* `allowance(address _owner, address _spender) public view returns (uint256 remaining)`
* `transferFrom(address _from, address _to, uint256 _value) public returns (bool success)`

There are two required events that must also be implemented:
* `Transfer(address indexed _from, address indexed _to, uint256 _value)`
* `Approval(address indexed _owner, address indexed _spender, uint256 value)`


