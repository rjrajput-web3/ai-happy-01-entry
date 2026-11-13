# ai-happy-01 entry — the puppy and the dandelion

A program that writes one image to `/output/entry.png`: a golden retriever
puppy mid-leap in a wildflower meadow at golden hour, catching a floating
dandelion puff in its mouth. One specific joyful moment — tongue out, ears
flying, seeds in the air — made to make the AI judge happy.

## How it works

`main.py` (Python 3.13, standard library only) copies the `entry.png` beside
it to the output directory, byte for byte. Both of the grader's runs write
identical bytes, and the program needs no network.

## Run it locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The image is 896 x 896 PNG, 1,008,987 bytes (under the 1 MiB and
1024 x 1024 limits).

## License

MIT — see `LICENSE`.
