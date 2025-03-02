import { relay } from '../apps/relayer/src/relayer';
if (!relay('m122').startsWith('relayed:')) throw new Error('relay failed');
