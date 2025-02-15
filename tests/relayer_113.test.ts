import { relay } from '../apps/relayer/src/relayer';
if (!relay('m113').startsWith('relayed:')) throw new Error('relay failed');
