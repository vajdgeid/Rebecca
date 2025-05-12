import { relay } from '../apps/relayer/src/relayer';
if (!relay('m148').startsWith('relayed:')) throw new Error('relay failed');
