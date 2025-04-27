import { relay } from '../apps/relayer/src/relayer';
if (!relay('m142').startsWith('relayed:')) throw new Error('relay failed');
