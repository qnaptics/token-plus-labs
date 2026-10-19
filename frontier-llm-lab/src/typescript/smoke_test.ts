// Copyright (c) 2026 Qnaptics
// SPDX-License-Identifier: MIT

import "dotenv/config";
import OpenAI from "openai";

const apiKey = process.env.OPENAI_API_KEY;
if (!apiKey) {
  throw new Error("Missing OPENAI_API_KEY in .env");
}

const client = new OpenAI({ apiKey });
const model = process.env.OPENAI_MODEL ?? "gpt-6-luna";

const response = await client.responses.create({
  model,
  input:
    "In two sentences, explain why a model benchmark needs both quality and cost measurements.",
  max_output_tokens: 120,
});

console.log("Model:", model);
console.log("Response ID:", response.id);
console.log("Usage:", response.usage);
console.log("Output:", response.output_text);
