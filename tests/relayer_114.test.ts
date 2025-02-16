import { relay } from '../apps/relayer/src/relayer';
if (!relay('m114').startsWith('relayed:')) throw new Error('relay failed');
