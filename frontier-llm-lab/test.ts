import "dotenv/config";

console.log("CWD", process.cwd());
console.log("OPENAI_API_KEY present?", Boolean(process.env.OPENAI_API_KEY));
