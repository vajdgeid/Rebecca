# Architecture Overview

This repository implements a cross-chain bridge composed of:
- MultiSig on-chain bridge (Solidity) that authorizes messages via threshold approvals.
- Relayer service that verifies proofs and forwards messages.
- TypeScript SDK for message creation and client-side verification helpers.
- CI pipeline validating unit tests (Vitest), linting (Solhint) and Foundry tests.

Data flow:
1. Client creates a BridgeMessage via SDK.
2. Validators (owners) approve the message on-chain in MultiSigBridge.
3. Relayer observes approvals and triggers execution once threshold is met.
4. Destination chain releases/mints the asset (not implemented in this skeleton).

Security highlights:
- Threshold-based approvals, no single point of failure.
- Code linted and tested in CI.
