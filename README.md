# Folder Audit CLI

Build a small command-line tool that audits a folder without changing its
contents. The finished program will count file types, calculate the total
size, show the largest files, and optionally save a JSON report.

## Target command

Run commands from the repository root:

```bash
python -m folder_audit sample_inbox
python -m folder_audit sample_inbox --top 2
python -m folder_audit sample_inbox --include-hidden
python -m folder_audit sample_inbox --json reports/audit.json
```

The final output should look similar to this:

```text
Files: 5
Total size: 1.2 KB

Extensions:
  .txt: 2
  .csv: 1
  .log: 1
  [no extension]: 1

Largest files:
  620 B  data/users.csv
  310 B  logs/app.log
```

Exact sizes depend on the files being scanned.

## Definition of done

- Hidden files are skipped unless `--include-hidden` is present.
- Symbolic links are skipped.
- Results are deterministic: paths and extension names have a stable order.
- A missing path, a regular file used as the target, and an inaccessible
  folder produce readable errors instead of tracebacks.
- `--top` accepts only a positive integer.
- A successful command returns exit code `0`; a handled error returns `2`.
- The scanner never modifies the audited folder.
