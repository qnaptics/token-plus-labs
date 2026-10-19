# Day 1 — Frontier AI Mastery

## Objective
Establish a reproducible experimental environment for frontier-model
evaluation, evidence-grounded scientific QA, and cost-performance analysis.

## Implementation
- Python: experiment runner and evaluation
- TypeScript: API integration smoke test
- API: OpenAI Responses API
- Benchmark domain: scientific evidence-grounded question answering

## Execution Status
- [x] Python file executed
- [x] TypeScript file executed
- [ ] Raw Python benchmark output verified
- [ ] TypeScript output preserved as a research artifact
- [ ] Manual answer review completed
- [ ] Model cost and latency measurements verified

## Benchmark Cases

1. sci_001 — Mean comparison and statistical significance
2. sci_002 — Cell-culture results versus human efficacy
3. sci_003 — Missing survival outcome evidence

The initial dataset is synthetic. It is intended to test evidence
discipline, not to establish biomedical facts.

## Results

Record measured results in results/day_01_summary.md.
Do not infer accuracy, cost, or latency from successful execution alone.

### Questions for manual review

- Did the answer accurately reflect the supplied passage?
- Did it distinguish evidence from inference?
- Did it explicitly identify missing information?
- Did any supporting quote fail to support the conclusion?
- Did the model make claims beyond the evidence?

## Limitations
- Small initial dataset.
- Synthetic passages.
- Manual evaluation is not independent scientific validation.
- No general model ranking can be inferred from these cases.
- Pricing and model access must be verified before comparing costs.

## Day 1 Lessons
The API smoke tests establish basic integration.
Scientific reliability requires separate measurements of correctness,
evidence support, uncertainty handling, latency, and cost.

## Day 2 Plan
- Expand the benchmark.
- Compare two accessible models on identical cases.
- Keep prompts and evaluation criteria consistent.
- Record model identifiers, token usage, latency, and estimated cost.
- Review failures and calculate cost per successful answer.
