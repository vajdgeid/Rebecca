# SDK & Relayer API

## SDK
- `version(): string`
- `createMessage(source, target, asset, amount, recipient): BridgeMessage`
- `verifyMultiSig({ threshold, signatures }): boolean`

## Relayer
- `verifyProof(proof: string): boolean`
- `relay(message: string): string`
- `verifyMultiSigOnRelayer({ threshold, signatures }): boolean`

## Contracts
- `MultiSigBridge`
  - `propose(bytes payload) -> id`
  - `approve(bytes32 id)`
  - `execute(bytes32 id)`
