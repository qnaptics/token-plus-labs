# Copyright (c) 2026 Qnatics 
# SPDX-License-Identifier: MIT

import json
import os
import time
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT / "data" / "benchmark.jsonl"
RESULTS_PATH = ROOT / "results" / "baseline.jsonl"

load_dotenv(ROOT / ".env")

MODEL = os.getenv("OPENAI_MODEL", "gpt-6-luna")
client = OpenAI()

# Illustrative standard short-context rates in USD per 1M tokens.
# Verify current rates before relying on cost comparisons.
PRICE_PER_MILLION = {
    "gpt-6-luna": {"input": 0.10, "output": 0.50},
    "gpt-6.1-sol": {"input": 2.00, "output": 10.00},
}


def load_cases():
    with DATA_PATH.open(encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def estimate_cost(model, input_tokens, output_tokens):
    rates = PRICE_PER_MILLION.get(model)
    if rates is None:
        return None

    return (
        input_tokens * rates["input"]
        + output_tokens * rates["output"]
    ) / 1_000_000


def run_case(case):
    prompt = f"""
Answer using only the supplied passage.
Do not add outside facts.
If the passage does not support a conclusion, explicitly say what is unknown.
Distinguish observed findings from conclusions that the evidence cannot establish.

PASSAGE:
{case["passage"]}

QUESTION:
{case["question"]}

Return:
1. Answer
2. Supporting quote from the passage, or "No supporting quote"
3. Limitation or uncertainty, if applicable
""".strip()

    start = time.perf_counter()

    try:
        response = client.responses.create(
            model=MODEL,
            instructions=(
                "You are a careful scientific evidence analyst. "
                "Be concise, evidence-grounded, and explicit about uncertainty."
            ),
            input=prompt,
            max_output_tokens=300,
        )

        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        usage = response.usage

        input_tokens = usage.input_tokens if usage else 0
        output_tokens = usage.output_tokens if usage else 0

        return {
            "case_id": case["id"],
            "model": MODEL,
            "prompt_version": "v1",
            "latency_ms": latency_ms,
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "estimated_cost_usd": estimate_cost(
                MODEL, input_tokens, output_tokens
            ),
            "expected_behavior": case["expected_behavior"],
            "expected_answer": case["expected_answer"],
            "output": response.output_text,
            "response_id": response.id,
            "error": None,
        }

    except Exception as exc:
        return {
            "case_id": case["id"],
            "model": MODEL,
            "prompt_version": "v1",
            "latency_ms": round((time.perf_counter() - start) * 1000, 2),
            "error": f"{type(exc).__name__}: {exc}",
        }


def main():
    cases = load_cases()
    RESULTS_PATH.parent.mkdir(parents=True, exist_ok=True)

    # Append mode preserves earlier runs; use a new output filename
    # when you want a clean, independently comparable experiment.
    with RESULTS_PATH.open("a", encoding="utf-8") as out:
        for case in cases:
            result = run_case(case)
            out.write(json.dumps(result, ensure_ascii=False) + "\n")

            print(f'\n[{case["id"]}]')
            print("ERROR:", result.get("error"))
            if result.get("output"):
                print(result["output"])
            if result.get("estimated_cost_usd") is not None:
                print("Estimated cost USD:", result["estimated_cost_usd"])
            print("Latency ms:", result["latency_ms"])


if __name__ == "__main__":
    main()
