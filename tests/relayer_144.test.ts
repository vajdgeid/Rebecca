import { relay } from '../apps/relayer/src/relayer';
if (!relay('m144').startsWith('relayed:')) throw new Error('relay failed');
