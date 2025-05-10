import { relay } from '../apps/relayer/src/relayer';
if (!relay('m147').startsWith('relayed:')) throw new Error('relay failed');
