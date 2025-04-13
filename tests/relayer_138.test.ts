import { relay } from '../apps/relayer/src/relayer';
if (!relay('m138').startsWith('relayed:')) throw new Error('relay failed');
