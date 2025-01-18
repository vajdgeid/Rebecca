import { relay } from '../apps/relayer/src/relayer';
if (!relay('m104').startsWith('relayed:')) throw new Error('relay failed');
