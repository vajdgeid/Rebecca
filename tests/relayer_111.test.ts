import { relay } from '../apps/relayer/src/relayer';
if (!relay('m111').startsWith('relayed:')) throw new Error('relay failed');
