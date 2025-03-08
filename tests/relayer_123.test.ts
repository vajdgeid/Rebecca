import { relay } from '../apps/relayer/src/relayer';
if (!relay('m123').startsWith('relayed:')) throw new Error('relay failed');
