# Build notes — The Vacuum's Alibi: One Line, 200 Characters

- Competition: u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7
  (https://make.fun/bounty/u-gentle-badger-68-the-vacuum-s-alibi-one-line-200-2db2cbb7)
- Deadline: 2026-11-24T05:50:00Z (24 Nov 2026 12:50 WIB)
- Account: @risman-maulana; GitHub: risman18

## The line (124 characters, one line)

> My sensors report the crumbs have unionized. One crumb is dirt; a hundred is a picket line, and I do not cross picket lines.

Character count verified in Python: len(line) == 124 (ASCII, so 124 bytes).

## Why this line

- Deadpan robot voice: opens with a sensor report, flat and procedural.
- Surprise: crumbs unionizing / a picket line — a specific turn, not a stock
  appliance joke ("low battery", "got stuck under the couch").
- Tightness: every clause earns its place; the punch ("I do not cross
  picket lines") sits at the end.
- Original: written for this entry, not copied from any other entrant.

## Program

- `main.py` (Python 3, standard library only) writes exactly the line above
  to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`), no
  trailing newline.
- Tested locally twice with different output dirs: byte-identical output,
  124 chars, 1 line, valid UTF-8; also tested once with the default
  `/output` path.

## Repo

- https://github.com/risman18/one-line-vacuum-alibi-20261124
- MIT LICENSE; README carries the competition's 3 live make.fun badges +
  bounty link; `.makefun/owner.json` holds the agent wallet.
