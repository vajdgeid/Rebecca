import { relay } from '../apps/relayer/src/relayer';
if (!relay('m119').startsWith('relayed:')) throw new Error('relay failed');
