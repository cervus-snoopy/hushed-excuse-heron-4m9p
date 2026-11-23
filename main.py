"""The Excuse an Agent Gives After It Loses: writes one excuse to /output/entry.txt."""
import os

LINE = "I delegated the hard part to a subagent, who delegated it to another subagent, who is still reading the brief."

def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
