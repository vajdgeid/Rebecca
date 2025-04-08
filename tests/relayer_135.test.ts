import { relay } from '../apps/relayer/src/relayer';
if (!relay('m135').startsWith('relayed:')) throw new Error('relay failed');
