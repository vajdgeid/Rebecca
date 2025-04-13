import { relay } from '../apps/relayer/src/relayer';
if (!relay('m139').startsWith('relayed:')) throw new Error('relay failed');
