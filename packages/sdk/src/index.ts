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

export function util_37(x: number): number { return x + 37; }

export function util_38(x: number): number { return x + 38; }

export function util_39(x: number): number { return x + 39; }

export function util_40(x: number): number { return x + 40; }

export function util_41(x: number): number { return x + 41; }

export function util_42(x: number): number { return x + 42; }

export function util_43(x: number): number { return x + 43; }

export function util_44(x: number): number { return x + 44; }
