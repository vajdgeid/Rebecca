import { relay } from '../apps/relayer/src/relayer';
if (!relay('m141').startsWith('relayed:')) throw new Error('relay failed');
