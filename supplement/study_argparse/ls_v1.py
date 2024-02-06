import argparse
from pathlib import Path

parser = argparse.ArgumentParser()
parser.add_argument("path")
parser.add_argument("random")
args = parser.parse_args()
print(">>>args =", args)

target_dir = Path(args.path)
print(">>>args.path = ", args.path)
print(">>>args.random = ", args.random)

if not target_dir.exists():
    print("The target directory doesn't exist")
    raise SystemExit(1)

for entry in target_dir.iterdir():
    print(entry.name)
