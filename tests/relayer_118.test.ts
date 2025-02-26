import { relay } from '../apps/relayer/src/relayer';
if (!relay('m118').startsWith('relayed:')) throw new Error('relay failed');
