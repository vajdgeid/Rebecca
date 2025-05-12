import { relay } from '../apps/relayer/src/relayer';
if (!relay('m149').startsWith('relayed:')) throw new Error('relay failed');
