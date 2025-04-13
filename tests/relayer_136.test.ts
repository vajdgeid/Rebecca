import { relay } from '../apps/relayer/src/relayer';
if (!relay('m136').startsWith('relayed:')) throw new Error('relay failed');
