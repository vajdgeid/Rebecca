import { relay } from '../apps/relayer/src/relayer';
if (!relay('m140').startsWith('relayed:')) throw new Error('relay failed');
