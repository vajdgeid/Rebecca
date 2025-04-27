import { relay } from '../apps/relayer/src/relayer';
if (!relay('m143').startsWith('relayed:')) throw new Error('relay failed');
