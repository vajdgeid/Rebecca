import { relay } from '../apps/relayer/src/relayer';
if (!relay('m128').startsWith('relayed:')) throw new Error('relay failed');
