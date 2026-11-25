import os

ENTRY = "I didn't miss the deadline — it filed a restraining order against me, so legally I couldn't come within fifty feet of it."


def main():
    text = ENTRY
    if not text or not text.strip():
        raise SystemExit("entry is blank")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not 1 <= len(text) <= 200:
        raise SystemExit("entry must be 1-200 characters")
    if not 1 <= len(text.encode("utf-8")) <= 200:
        raise SystemExit("entry must be 1-200 UTF-8 bytes")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} chars, {len(text.encode('utf-8'))} bytes to {path}")


if __name__ == "__main__":
    main()
