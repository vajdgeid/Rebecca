import { relay } from '../apps/relayer/src/relayer';
if (!relay('m150').startsWith('relayed:')) throw new Error('relay failed');
