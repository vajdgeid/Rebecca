import { describe, it, expect } from 'vitest';
import { verifyProof, relay, verifyMultiSigOnRelayer } from '../../apps/relayer/src/relayer';

describe('Relayer', () => {
  it('verifies simple proof', () => {
    expect(verifyProof('proof')).toBe(true);
  });
  it('relays message and checks multisig threshold', () => {
    expect(relay('m')).toContain('relayed:');
    expect(verifyMultiSigOnRelayer({ threshold: 2, signatures: ['a','b'] })).toBe(true);
  });
});
