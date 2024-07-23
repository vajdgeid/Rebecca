// Relayer skeleton
export function verifyProof(proof: string): boolean { return proof.length > 0; }
export function relay(message: string): string { return `relayed:${message}`; }

export function handle_30(m: string): string { return m + '30'; }
