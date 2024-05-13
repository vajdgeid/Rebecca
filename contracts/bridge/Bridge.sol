// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Bridge {
    event Locked(address indexed user, uint256 amount, string targetChain);
    function lock(uint256 amount, string memory targetChain) external {
        emit Locked(msg.sender, amount, targetChain);
    }
}
