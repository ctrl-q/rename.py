#!/usr/bin/env python3

import re
from pathlib import Path
import sys



def parse_args():
    from argparse import ArgumentParser

    parser = ArgumentParser()
    parser.add_argument("-v", "--verbose", action="store_true", help="explain what is being done")
    overwrite_group = parser.add_mutually_exclusive_group()
    overwrite_group.add_argument("-n", "--no-act", action="store_true", help="do not make any changes")
    overwrite_group.add_argument("-o", "--no-overwrite", action="store_true", help="dont overwrite existing files")
    overwrite_group.add_argument("-i", "--interactive", action="store_true", help="prompt before overwrite")
    parser.add_argument("-r", "--regex", action="store_true", help="pattern is regex")
    parser.add_argument("expression")
    parser.add_argument("replacement")
    parser.add_argument("file", nargs="+", type=Path)

    args = parser.parse_args()
    return args


def replace(path, replacement, args):
    if path == replacement:
        if args.verbose:
            print(f"File {str(path)} is already named {str(replacement)}, skipping", file=sys.stderr)
        return
    elif args.no_act:
        if args.verbose:
            print(str(path), "->", str(replacement), " (dry run)", file=sys.stderr)
        return
    if replacement.exists():
        if args.interactive:
            should_replace = input(f"Replace {str(path)} with {str(replacement)} ? (Y/n) ").lower()
            match should_replace:
                case "y": pass
                case "n": return
                case _:
                    raise ValueError("Invalid answer")
        elif args.no_overwrite:
            print(f"File {str(replacement)} already exists, skipping {str(path)}", file=sys.stderr)
            return
    path.replace(replacement)
    if args.verbose:
        print(str(file), "->", str(replacement), file=sys.stderr)


def main():
    from functools import partial

    args = parse_args()
    get_replacement = partial(re.compile(args.expression).sub, args.replacement) if args.regex else lambda s: s.replace(args.expression, args.replacement)

    for file in args.file:
        replacement = Path(get_replacement(str(file)))
        try:
            replace(file, replacement, args)
        except Exception as e:
            print(f"Error replacing {str(file)} with {str(replacement)}: {e}", file=sys.stderr)
            exit(1)

if __name__ == "__main__":
    main()
