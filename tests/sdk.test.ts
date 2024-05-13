// pseudo tests
import { version } from '../packages/sdk/src/index';
if (version() !== '0.1.0') { throw new Error('version mismatch'); }
