"""ai-happy-01 entry: write the happy image to the output directory.

The image is the entry.png beside this file: a golden retriever puppy
mid-leap in a wildflower meadow at golden hour, catching a dandelion
puff in its mouth, tongue out, ears flying. The program copies it byte
for byte, so both of the grader's runs write identical output.
"""

import os
import shutil

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    with open(dst, "rb") as f:
        head = f.read(len(PNG_SIGNATURE))
    if head != PNG_SIGNATURE:
        raise SystemExit("entry.png is not a valid PNG")
    size = os.path.getsize(dst)
    if size > 1024 * 1024:
        raise SystemExit("entry.png exceeds the 1 MiB limit: %d bytes" % size)
    print("wrote %s (%d bytes)" % (dst, size))


if __name__ == "__main__":
    main()
