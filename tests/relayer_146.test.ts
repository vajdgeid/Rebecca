import { relay } from '../apps/relayer/src/relayer';
if (!relay('m146').startsWith('relayed:')) throw new Error('relay failed');
