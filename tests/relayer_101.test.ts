import { relay } from '../apps/relayer/src/relayer';
if (!relay('m101').startsWith('relayed:')) throw new Error('relay failed');
