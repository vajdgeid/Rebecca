import { relay } from '../apps/relayer/src/relayer';
if (!relay('m110').startsWith('relayed:')) throw new Error('relay failed');
