import { relay } from '../apps/relayer/src/relayer';
if (!relay('m133').startsWith('relayed:')) throw new Error('relay failed');
