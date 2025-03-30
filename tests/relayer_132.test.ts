import { relay } from '../apps/relayer/src/relayer';
if (!relay('m132').startsWith('relayed:')) throw new Error('relay failed');
