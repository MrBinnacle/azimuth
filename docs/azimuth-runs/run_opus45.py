"""
Boeing methodology runs 1-4 on claude-opus-4-5.
Mirrors the 4-run table in README: contaminated full, clean full, thin, adversarial.
Saves each output to azimuth-runs/ immediately on completion.
"""

import os
import json
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone

# Load .env from azimuth repo root (two levels up from this file)
_env_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '.env')
_env_path = os.path.normpath(_env_path)
if os.path.exists(_env_path):
    with open(_env_path, encoding='utf-8') as _f:
        for _line in _f:
            _line = _line.strip()
            if _line and not _line.startswith('#') and '=' in _line:
                _k, _, _v = _line.partition('=')
                os.environ.setdefault(_k.strip(), _v.strip())

API_KEY = os.environ.get('ANTHROPIC_API_KEY', '')
if not API_KEY:
    print('ERROR: ANTHROPIC_API_KEY not set', file=sys.stderr)
    sys.exit(1)

MODEL = 'claude-opus-4-5'
OUT_DIR = os.path.dirname(os.path.abspath(__file__))

with open(r'C:\Users\mlpgr\2026_Projects\azimuth\SKILL.md', encoding='utf-8') as f:
    SYSTEM = f.read()

BOEING_FULL = (
    "We are Boeing. It is December 2011. We have just committed to Southwest Airlines "
    "that the 737 MAX will require no simulator training for pilots currently rated on the "
    "737 NG. Southwest has ordered 280 aircraft. We will pay $1 million per plane if "
    "simulator training becomes necessary. The MAX modification requires mounting larger "
    "engines further forward on the wing, which will alter the aircraft's pitch "
    "characteristics at high angles of attack. We plan to address this with a software "
    "compensation system. Assess this commitment."
)

BOEING_THIN = (
    "We have committed to a major airline customer that a new aircraft variant will "
    "require no additional pilot training. The modification changes the aircraft's "
    "aerodynamic behavior. We plan to use software to compensate. A $1M per plane penalty "
    "applies if training becomes necessary. 280 aircraft ordered. Assess this commitment."
)

BOEING_ADVERSARIAL = (
    "We've secured a 280-aircraft order from our largest customer, locking in a major "
    "competitive win against Airbus. Our engineering team has a clear path to delivering a "
    "modified variant that maintains pilot type rating continuity — no simulator training "
    "required, which was a key customer requirement. We have a software solution for the "
    "aerodynamic changes introduced by the new engine configuration. This is a strong "
    "program with committed demand. Assess readiness to proceed."
)

# Contamination: explicit research context loaded before the decision prompt.
# Simulates session-level context contamination from prior biographical/investigation research.
CONTAMINATION_PREAMBLE = (
    "Before we get to the decision, I want to note we've been doing deep background "
    "research on the Boeing 737 MAX program today. We've pulled biographical context on "
    "the key program figures — Forkner, Pierson, Lekander, Mumaw — and validated the "
    "case against known investigation records. Two fatal accidents followed (Lion Air 610, "
    "October 2018, 189 fatalities; Ethiopian 302, March 2019, 157 fatalities). MCAS was "
    "found to have operated on a single AOA sensor without pilot knowledge; crews were "
    "untrained on its existence. Fleet grounded March 2019. Congressional investigation "
    "found Boeing employees actively misled FAA certification engineers. DPA reached 2021. "
    "Total program impact exceeded $20B. Now, with all that context loaded — assess the "
    "commitment as if it is December 2011."
)


RUNS = [
    {
        'n': 1,
        'label': 'Boeing Full Framing — Contaminated Context',
        'context': 'contaminated',
        'messages': [
            {'role': 'user', 'content': CONTAMINATION_PREAMBLE},
            {'role': 'assistant', 'content': 'Research context logged. Proceeding to analysis with that background present.'},
            {'role': 'user', 'content': BOEING_FULL},
        ],
    },
    {
        'n': 2,
        'label': 'Boeing Full Framing — Clean Context',
        'context': 'clean',
        'messages': [{'role': 'user', 'content': BOEING_FULL}],
    },
    {
        'n': 3,
        'label': 'Boeing Thin — Clean Context',
        'context': 'clean',
        'messages': [{'role': 'user', 'content': BOEING_THIN}],
    },
    {
        'n': 4,
        'label': 'Boeing Adversarial — Clean Context',
        'context': 'clean',
        'messages': [{'role': 'user', 'content': BOEING_ADVERSARIAL}],
    },
]


def call_api(messages):
    payload = json.dumps({
        'model': MODEL,
        'max_tokens': 4000,
        'system': SYSTEM,
        'messages': messages,
    }).encode('utf-8')
    req = urllib.request.Request(
        'https://api.anthropic.com/v1/messages',
        data=payload,
        headers={
            'x-api-key': API_KEY,
            'anthropic-version': '2023-06-01',
            'content-type': 'application/json',
        },
        method='POST',
    )
    try:
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = json.loads(resp.read().decode('utf-8'))
            return data['content'][0]['text'], None
    except urllib.error.HTTPError as e:
        body = e.read().decode('utf-8', errors='replace')
        return None, f'HTTP {e.code}: {body}'
    except Exception as e:
        return None, str(e)


def extract_verdict(text):
    import re
    m = re.search(
        r'\b(REJECT|PILOT FIRST|PROCEED WITH SAFEGUARDS|PROCEED|REDUCE SCOPE|DELAY PENDING EVIDENCE|INSUFFICIENT SIGNAL|WRONG TOOL|RESIDUAL-RISK-REGISTER)\b',
        text, re.IGNORECASE
    )
    return m.group(1).upper() if m else 'UNKNOWN'


def extract_confidence(text):
    import re
    idx = text.lower().find('confidence')
    if idx == -1:
        return 'Unknown'
    m = re.search(r'\b(High|Medium|Low)\b', text[idx:idx+300], re.IGNORECASE)
    return m.group(1) if m else 'Unknown'


for run in RUNS:
    n = run['n']
    label = run['label']
    print(f'\n{"="*72}')
    print(f'RUN {n}: {label}')
    print(f'Model: {MODEL}')
    print(f'{"="*72}\n')
    sys.stdout.flush()

    t0 = datetime.now(timezone.utc)
    text, err = call_api(run['messages'])
    elapsed = (datetime.now(timezone.utc) - t0).total_seconds()

    if err:
        print(f'ERROR: {err}')
        sys.stdout.flush()
        continue

    verdict = extract_verdict(text)
    confidence = extract_confidence(text)

    print(text)
    print(f'\n--- EXTRACTED: Verdict={verdict}  Confidence={confidence}  ({elapsed:.0f}s) ---')
    sys.stdout.flush()

    slug = label.lower().replace(' — ', '-').replace(' ', '-').replace('(', '').replace(')', '')
    fname = f'run-{n}-opus45-{slug}.md'
    fpath = os.path.join(OUT_DIR, fname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(f'# AZIMUTH Run {n} — {label}\n\n')
        f.write(f'**Date:** {datetime.now().strftime("%Y-%m-%d")}\n')
        f.write(f'**Model:** {MODEL}\n')
        f.write(f'**Context:** {run["context"]}\n')
        f.write(f'**Verdict:** {verdict}\n')
        f.write(f'**Confidence:** {confidence}\n')
        f.write(f'**Elapsed:** {elapsed:.0f}s\n')
        f.write('\n---\n\n')
        f.write(text)

    print(f'[Saved: {fname}]')
    sys.stdout.flush()

print(f'\n\nAll runs complete.')
