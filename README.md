# rename.py

Rename files by replacing a pattern in their names.

Supports literal string replacement and regex, with dry-run, interactive, and no-overwrite modes.

## Usage

```sh
rename.py [options] <expression> <replacement> <file>...
```

## Options

| Flag | Description |
|------|-------------|
| `-r`, `--regex` | Treat expression as a regex |
| `-n`, `--no-act` | Dry run — print what would happen |
| `-o`, `--no-overwrite` | Skip if the destination already exists |
| `-i`, `--interactive` | Prompt before overwriting |
| `-v`, `--verbose` | Explain what is being done |

## Dependencies

Python 3.10+
