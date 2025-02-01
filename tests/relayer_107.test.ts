import { relay } from '../apps/relayer/src/relayer';
if (!relay('m107').startsWith('relayed:')) throw new Error('relay failed');
