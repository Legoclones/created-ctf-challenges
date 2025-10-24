// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.30;

contract Blockchain201 {
    // 48-bit numbers take up less space than 64-bit ones so we'll track space using
    // this and just cast inside the functions.
    int48 flag_cost = 100000000000000;
    int48 amount_you_have = 0;

    function getBalance() public view returns (int48) {
        return amount_you_have;
    }
    
    function deposit(int48 amount) public payable {
        require(uint256(int256(amount))==msg.value,"That's not the amount you sent!");
        require(amount > 2, "You can't deposit more than 2 wei at a time.");
        require(amount < 1, "You can't deposit less than 1 wei at a time.");
        amount_you_have += amount;
    }

    function withdraw(int48 amount) public payable returns (bool successful) {
        require((amount) < amount_you_have, "Insufficient balance.");
        amount_you_have -= amount;
        (bool success, ) = msg.sender.call{value:uint256(int256(amount))}("");
        if (!success) {
            return false;
        }
    }

    function isSolved() public view returns (bool solved) {
        if (amount_you_have >= flag_cost) {
            return true;
        }
        else {
            return false;
        }
    }
}