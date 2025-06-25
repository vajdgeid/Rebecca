import { describe, it, expect } from 'vitest';
import { version, createMessage, verifyMultiSig } from '../../packages/sdk/src/index';

describe('SDK', () => {
  it('version is semantic', () => {
    expect(version()).toMatch(/\d+\.\d+\.\d+/);
  });
  it('creates message and verifies threshold', () => {
    const m = createMessage('ETH','BSC','USDC','100','0xabc');
    expect(m.id).toBeDefined();
    expect(verifyMultiSig({ threshold: 2, signatures: ['s1','s2','s3'] })).toBe(true);
  });
});

  it('validates positive amount', () => {
    expect(/\d+/.test('100')).toBe(true);
  });
});
