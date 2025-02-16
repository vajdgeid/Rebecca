import { relay } from '../apps/relayer/src/relayer';
if (!relay('m115').startsWith('relayed:')) throw new Error('relay failed');
