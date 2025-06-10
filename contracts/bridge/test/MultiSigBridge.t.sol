// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "forge-std/Test.sol";
import { MultiSigBridge } from "../src/MultiSigBridge.sol";

contract MultiSigBridgeTest is Test {
    MultiSigBridge bridge;
    address a = address(0xA1);
    address b = address(0xB2);
    address c = address(0xC3);

    function setUp() public {
        address[] memory owners = new address[](3);
        owners[0] = a; owners[1] = b; owners[2] = c;
        bridge = new MultiSigBridge(owners, 2);
    }

    function testProposeApproveExecute() public {
        vm.prank(a);
        bytes memory payload = abi.encodePacked("lock:ETH->BSC:100");
        bytes32 id = bridge.propose(payload);
        vm.prank(b);
        bridge.approve(id);
        bridge.execute(id);
        // If no revert, execution succeeded under threshold 2
        assertTrue(true);
    }
}
