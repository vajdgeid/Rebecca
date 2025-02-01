import { relay } from '../apps/relayer/src/relayer';
if (!relay('m109').startsWith('relayed:')) throw new Error('relay failed');
