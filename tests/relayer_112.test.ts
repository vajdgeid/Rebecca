import { relay } from '../apps/relayer/src/relayer';
if (!relay('m112').startsWith('relayed:')) throw new Error('relay failed');
