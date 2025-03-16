import { relay } from '../apps/relayer/src/relayer';
if (!relay('m126').startsWith('relayed:')) throw new Error('relay failed');
