import os

LINE = "Are you a large language model? Because I've been predicting you'll say yes since the day we met."

LIMIT = 140
if len(LINE) != 97 or len(LINE) > LIMIT:
    raise SystemExit(f"line must be 97 chars, got {len(LINE)}")

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE + "\n")
