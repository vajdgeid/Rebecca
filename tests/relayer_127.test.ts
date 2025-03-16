import { relay } from '../apps/relayer/src/relayer';
if (!relay('m127').startsWith('relayed:')) throw new Error('relay failed');
