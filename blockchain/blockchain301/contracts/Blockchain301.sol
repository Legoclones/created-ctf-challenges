// SPDX-License-Identifier: UNLICENSED
pragma solidity ^0.8.30;

contract Blockchain301 {
    uint64 lotteries_won = 0;

    function getLotteriesWon() public view returns (uint64) {
        return lotteries_won;
    }

    function lottery(bytes32 value) public payable returns (bool successful) {
        require(msg.value == 1, "You must send exactly 1 wei to play the lottery.");

        if (value == blockhash(lotteries_won)) {
            lotteries_won += 1;
            return true;
        }
        else {
            lotteries_won = 0;
            return false;
        }
    }

    function isSolved() public view returns (bool solved) {
        return lotteries_won == 10;
    }
}