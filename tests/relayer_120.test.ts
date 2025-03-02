import { relay } from '../apps/relayer/src/relayer';
if (!relay('m120').startsWith('relayed:')) throw new Error('relay failed');
