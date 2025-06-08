// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract MultiSigBridge {
    event MessageProposed(bytes32 indexed id, address indexed proposer, bytes payload);
    event Approved(bytes32 indexed id, address indexed approver, uint256 approvals);
    event Executed(bytes32 indexed id, bytes payload);

    address[] public owners;
    mapping(address => bool) public isOwner;
    uint256 public threshold;

    struct Proposal {
        bytes payload;
        uint256 approvals;
        bool executed;
        mapping(address => bool) approvedBy;
    }

    mapping(bytes32 => Proposal) private proposals;

    constructor(address[] memory _owners, uint256 _threshold) {
        require(_owners.length > 0, "no owners");
        require(_threshold > 0 && _threshold <= _owners.length, "bad threshold");
        for (uint256 i = 0; i < _owners.length; i++) {
            address o = _owners[i];
            require(o != address(0), "zero owner");
            require(!isOwner[o], "dup owner");
            isOwner[o] = true;
            owners.push(o);
        }
        threshold = _threshold;
    }

    function propose(bytes calldata payload) external returns (bytes32 id) {
        require(isOwner[msg.sender], "not owner");
        id = keccak256(abi.encode(payload));
        Proposal storage p = proposals[id];
        require(p.payload.length == 0, "exists");
        p.payload = payload;
        emit MessageProposed(id, msg.sender, payload);
        _approve(id);
    }

    function approve(bytes32 id) external {
        require(isOwner[msg.sender], "not owner");
        _approve(id);
    }

    function _approve(bytes32 id) internal {
        Proposal storage p = proposals[id];
        require(p.payload.length != 0, "no proposal");
        require(!p.executed, "executed");
        require(!p.approvedBy[msg.sender], "dup approve");
        p.approvedBy[msg.sender] = true;
        p.approvals += 1;
        emit Approved(id, msg.sender, p.approvals);
    }

    function execute(bytes32 id) external {
        Proposal storage p = proposals[id];
        require(p.payload.length != 0, "no proposal");
        require(!p.executed, "executed");
        require(p.approvals >= threshold, "insufficient");
        p.executed = true;
        emit Executed(id, p.payload);
        // bridging side effects would occur here (e.g., mint/release)
    }
}
