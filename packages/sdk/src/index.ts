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
