import { relay } from '../apps/relayer/src/relayer';
if (!relay('m103').startsWith('relayed:')) throw new Error('relay failed');
