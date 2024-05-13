#!/usr/bin/env python3
import csv
import os
import random
import subprocess
import sys
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path

WORKDIR = Path(os.getcwd())
CSV_PATH = WORKDIR / 'github_accounts.csv'
PROJECT_DIRS = {
    'frontend': WORKDIR / 'apps' / 'frontend' / 'src',
    'sdk': WORKDIR / 'packages' / 'sdk' / 'src',
    'relayer': WORKDIR / 'apps' / 'relayer' / 'src',
    'contracts': WORKDIR / 'contracts' / 'bridge',
    'tests': WORKDIR / 'tests',
}

PHASES = [
    ('init', 4),
    ('core', 10),
    ('test_opt', 8),
    ('docs_finish', 2),
]
PHASE_RATIO = [w / sum(w for _, w in PHASES) for _, w in PHASES]
PHASE_NAMES = [p for p, _ in PHASES]

START_DATE = datetime(2024, 5, 1, 9, 0, 0, tzinfo=timezone.utc)
END_DATE = datetime(2025, 6, 30, 18, 0, 0, tzinfo=timezone.utc)

@dataclass
class Account:
    username: str
    email: str


def read_accounts(csv_path: Path):
    accounts = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            username = (row.get('username') or '').strip()
            email = (row.get('email') or '').strip().strip('"')
            if username and email:
                accounts.append(Account(username=username, email=email))
    accounts.sort(key=lambda a: a.username)
    return accounts


def split_date_ranges(start: datetime, end: datetime):
    total = (end - start).total_seconds()
    edges = [start]
    acc = 0.0
    for r in PHASE_RATIO:
        acc += r
        edges.append(start + timedelta(seconds=total * acc))
    return [(edges[i], edges[i+1]) for i in range(len(PHASES))]


def commits_per_phase(total_commits: int):
    raw = [int(total_commits * r) for r in PHASE_RATIO]
    remainder = total_commits - sum(raw)
    i = 0
    while remainder > 0:
        raw[i % len(raw)] += 1
        remainder -= 1
        i += 1
    return raw


def spaced_times(start: datetime, end: datetime, n: int):
    if n <= 0:
        return []
    span = (end - start) / (n + 1)
    times = [start + span * (i + 1) for i in range(n)]
    out = []
    for t in times:
        jitter = timedelta(minutes=random.randint(-240, 240))
        tt = t + jitter
        if tt < start:
            tt = start + timedelta(minutes=random.randint(0, 240))
        if tt > end:
            tt = end - timedelta(minutes=random.randint(0, 240))
        out.append(tt)
    out.sort()
    return out


def git(*args, env=None):
    return subprocess.run(['git'] + list(args), cwd=str(WORKDIR), env=env, check=True, capture_output=True)


def ensure_baseline():
    created = []
    sdk_idx = PROJECT_DIRS['sdk'] / 'index.ts'
    sdk_idx.parent.mkdir(parents=True, exist_ok=True)
    sdk_idx.write_text(
        """// SDK entry
export type ChainId = 'ETH' | 'BSC' | 'POLY' | 'AVAX' | 'COSMOS' | 'DOT';

export interface BridgeTransfer {
  source: ChainId;
  target: ChainId;
  asset: string;
  amount: string;
  recipient: string;
}

export function version(): string {
  return '0.1.0';
}
""", encoding='utf-8')
    created.append(sdk_idx)

    rel_ts = PROJECT_DIRS['relayer'] / 'relayer.ts'
    rel_ts.parent.mkdir(parents=True, exist_ok=True)
    rel_ts.write_text(
        """// Relayer skeleton
export function verifyProof(proof: string): boolean { return proof.length > 0; }
export function relay(message: string): string { return `relayed:${message}`; }
""", encoding='utf-8')
    created.append(rel_ts)

    fe_api = PROJECT_DIRS['frontend'] / 'api.ts'
    fe_api.parent.mkdir(parents=True, exist_ok=True)
    fe_api.write_text(
        """// Frontend API facade
export async function createTransfer(): Promise<string> { return 'tx_0'; }
export async function getStatus(id: string): Promise<string> { return `status:${id}`; }
""", encoding='utf-8')
    created.append(fe_api)

    sol = PROJECT_DIRS['contracts'] / 'Bridge.sol'
    sol.parent.mkdir(parents=True, exist_ok=True)
    sol.write_text(
        """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

contract Bridge {
    event Locked(address indexed user, uint256 amount, string targetChain);
    function lock(uint256 amount, string memory targetChain) external {
        emit Locked(msg.sender, amount, targetChain);
    }
}
""", encoding='utf-8')
    created.append(sol)

    test_sdk = PROJECT_DIRS['tests'] / 'sdk.test.ts'
    test_sdk.parent.mkdir(parents=True, exist_ok=True)
    test_sdk.write_text(
        """// pseudo tests
import { version } from '../packages/sdk/src/index';
if (version() !== '0.1.0') { throw new Error('version mismatch'); }
""", encoding='utf-8')
    created.append(test_sdk)

    # Include baseline non-sensitive files if present
    for name in ['.gitignore', 'README.md', 'LICENSE', 'tools/invite_collaborators.py', 'tools/orchestrator.py']:
        p = WORKDIR / name
        if p.exists():
            created.append(p)

    return [str(p) for p in created]


def modify_code(phase: str, idx: int):
    if phase == 'init':
        p = PROJECT_DIRS['sdk'] / f'init_{idx}.ts'
        p.write_text(f"export const INIT_{idx}: number = {idx};\n", encoding='utf-8')
        return [str(p)]
    elif phase == 'core':
        sdk = PROJECT_DIRS['sdk'] / 'index.ts'
        with sdk.open('a', encoding='utf-8') as f:
            f.write(f"\nexport function util_{idx}(x: number): number {{ return x + {idx}; }}\n")
        rel = PROJECT_DIRS['relayer'] / 'relayer.ts'
        with rel.open('a', encoding='utf-8') as f:
            f.write(f"\nexport function handle_{idx}(m: string): string {{ return m + '{idx}'; }}\n")
        return [str(sdk), str(rel)]
    elif phase == 'test_opt':
        t = PROJECT_DIRS['tests'] / f'relayer_{idx}.test.ts'
        t.write_text(
            f"import {{ relay }} from '../apps/relayer/src/relayer';\nif (!relay('m{idx}').startsWith('relayed:')) throw new Error('relay failed');\n",
            encoding='utf-8')
        return [str(t)]
    else:
        fe = PROJECT_DIRS['frontend'] / f'widget_{idx}.ts'
        fe.write_text(f"export const WIDGET_{idx} = '{idx}';\n", encoding='utf-8')
        return [str(fe)]


def commit_change(files, message: str, when: datetime, author_name: str, author_email: str):
    git('add', '--', *files)
    env = os.environ.copy()
    fmt = when.strftime('%Y-%m-%d %H:%M:%S %z')
    env['GIT_AUTHOR_DATE'] = fmt
    env['GIT_COMMITTER_DATE'] = fmt
    git('-c', f'user.name={author_name}', '-c', f'user.email={author_email}',
        'commit', '-m', message, env=env)


def main():
    random.seed(1337)
    accounts = read_accounts(CSV_PATH)
    if not accounts:
        raise RuntimeError('No accounts parsed from CSV')

    baseline_files = ensure_baseline()

    windows = split_date_ranges(START_DATE, END_DATE)

    plan = []
    for acc in accounts:
        total = random.randint(20, 30)
        per_phase = commits_per_phase(total)
        for (phase_name, _), (w_start, w_end), n in zip(PHASES, windows, per_phase):
            times = spaced_times(w_start, w_end, n)
            for t in times:
                plan.append((t, acc, phase_name))

    plan.sort(key=lambda x: x[0])

    counter = 0
    for t, acc, phase in plan:
        counter += 1
        files = modify_code(phase, counter)
        if counter == 1:
            # include baseline files in the very first commit
            files = list(dict.fromkeys(baseline_files + files))
        if phase == 'init':
            prefix = 'feat'
        elif phase == 'core':
            prefix = random.choice(['feat', 'refactor', 'fix'])
        elif phase == 'test_opt':
            prefix = random.choice(['test', 'fix'])
        else:
            prefix = 'docs'
        msg = f"{prefix}: {phase} change #{counter}"
        commit_change(files, msg, t, acc.username, acc.email)

    print(f"created {counter} commits across {len(accounts)} accounts")


if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as e:
        sys.stderr.write(e.stderr.decode('utf-8', errors='ignore'))
        sys.exit(1)
    except Exception as e:
        print(f"error: {e}")
        sys.exit(1)
