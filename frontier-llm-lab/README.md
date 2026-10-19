# Frontier AI Mastery

A reproducible lab for frontier-model experiments, evaluation,
cost-performance engineering, and scientific AI.

## First experiment

Run a small evidence-grounded scientific QA benchmark.

### Python

python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python src/python/run_benchmark.py

### TypeScript

npm install
npx tsx src/typescript/smoke_test.ts

## Experiment principles

- Record the exact model ID and prompt version.
- Preserve raw outputs and token usage.
- Separate correctness from evidence support.
- Treat automated graders as imperfect.
- Record failures, not just successful examples.
- Do not make scientific or clinical claims from this toy benchmark.

## Security

Never commit .env or API keys.
