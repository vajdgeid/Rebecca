import { relay } from '../apps/relayer/src/relayer';
if (!relay('m117').startsWith('relayed:')) throw new Error('relay failed');
