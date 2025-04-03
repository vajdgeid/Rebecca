import { relay } from '../apps/relayer/src/relayer';
if (!relay('m134').startsWith('relayed:')) throw new Error('relay failed');
