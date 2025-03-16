import { relay } from '../apps/relayer/src/relayer';
if (!relay('m124').startsWith('relayed:')) throw new Error('relay failed');
