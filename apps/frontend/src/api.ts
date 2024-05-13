// Frontend API facade
export async function createTransfer(): Promise<string> { return 'tx_0'; }
export async function getStatus(id: string): Promise<string> { return `status:${id}`; }
