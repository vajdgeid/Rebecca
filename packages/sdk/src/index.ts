// SDK entry
export type ChainId = 'ETH' | 'BSC' | 'POLY' | 'AVAX' | 'COSMOS' | 'DOT';

export interface BridgeTransfer {
  source: ChainId;
  target: ChainId;
  asset: string;
  amount: string;
  recipient: string;
}

export function version(): string {
  return '0.1.0';
}

export function util_30(x: number): number { return x + 30; }

export function util_31(x: number): number { return x + 31; }

export function util_32(x: number): number { return x + 32; }

export function util_33(x: number): number { return x + 33; }

export function util_34(x: number): number { return x + 34; }

export function util_35(x: number): number { return x + 35; }

export function util_36(x: number): number { return x + 36; }
