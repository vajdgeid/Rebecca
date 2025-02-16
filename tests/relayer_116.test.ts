import { relay } from '../apps/relayer/src/relayer';
if (!relay('m116').startsWith('relayed:')) throw new Error('relay failed');
