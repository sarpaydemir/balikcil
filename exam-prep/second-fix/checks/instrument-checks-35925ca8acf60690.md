# Instrument checks — run `35925ca8acf60690`

Written by `scripts/25_instrument_checks.py`. Every number below is counted by that script.

| field | value |
|---|---|
| run number (RULES 29) | `35925ca8acf60690` |
| full input fingerprint | `35925ca8acf606904a9d969733e491cec9c269f44e6470ced74aa44619cd3f0d` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T19:12:43Z |
| free disk space at start (bytes) | 12496375808 |
| `scripts/25_instrument_checks.py` SHA-256 | `08bf00f6650ce7a4e08862860ffe17ba43e41448e4df855077acc01f820f6863` |

## E-1 · the changed blinding script reproduces every reviewed card

| variant | reviewed run | configuration | identical | different |
|---|---|---|---|---|
| `ratio` | `ca9e460829ecdac5` | `levels=ratio;btceth=drop;funding=summary;takerbuy=centred;p7=full;ratio_dp=3` | 306 | 0 |
| `rank` | `35df01d621d8da5a` | `levels=rank;btceth=drop;funding=summary;takerbuy=centred;p7=full;ratio_dp=3` | 306 | 0 |
| `strict` | `a9a8f3bcd515fd62` | `levels=rank;btceth=drop;funding=summary;takerbuy=rank;p7=no-scale;ratio_dp=3` | 306 | 0 |
| `strict-flags` | `10405ae115941d40` | `levels=rank;btceth=drop;funding=flags;takerbuy=rank;p7=no-scale;ratio_dp=3` | 306 | 0 |

## E-2 · what `chance_line()` accepts and refuses

| attempt | result | detail |
|---|---|---|
| events as a plain list of lists (the reviewed interface) | TypeError | "events must be an EventMap returned by collapse() or identity_map(), not a list" |
| identity partition typed as a plain list (REVIEW §4.3 bypass) | TypeError | "events must be an EventMap returned by collapse() or identity_map(), not a list" |
| identity_map(), block | accepted | {"config": "none/none/none", "mode": "block", "events": 306, "n_in_null": 306, "identity_partition": true, "event_map_sha256": "3d904d31acf871084d211e79f02a1c1cde63b88917433ffd733b569c9608c796", "immovable_events": 0, "cards_in_immovable_events": 0} |
| a start-hour map relabelled as card-span/component/any | ValueError | "the event map does not match what its own configuration card-span/component/any makes from its own moments" |
| a card-span map with one card removed from its events | ValueError | "the event map does not match what its own configuration card-span/component/any makes from its own moments" |
| mode omitted | TypeError | "chance_line() missing 1 required positional argument: 'mode'" |
| mode='card' | ValueError | "mode must be 'block' or 'representative'" |
| representative without `representatives` | ValueError | "representative mode needs `representatives`: one id per event, chosen by the caller" |
| representative naming two cards of one event | ValueError | "`representatives` must name exactly one card of every event" |
| card-span/component/any, block | accepted | {"config": "card-span/component/any", "mode": "block", "events": 58, "n_in_null": 306, "identity_partition": false, "event_map_sha256": "021cab6b1ab37fba28662247ee5525c4f9db0462f1f738eb8d2f7b5ec3fc1ce5", "immovable_events": 2, "cards_in_immovable_events": 23} |
| card-span/component/any, representative (first id of each event, a test choice only) | accepted | {"config": "card-span/component/any", "mode": "representative", "events": 58, "n_in_null": 58, "identity_partition": false, "event_map_sha256": "021cab6b1ab37fba28662247ee5525c4f9db0462f1f738eb8d2f7b5ec3fc1ce5"} |
| old-style unpacking `observed, boundary, null = chance_line(...)` | ValueError | "too many values to unpack (expected 3, got 17)" |

## E-3 · K-4, the granularity probe on the rebased `close`

One feature: the smallest non-zero difference between two printed `close` values of a card. The audit's two attacks, 1,000 shuffles, best 1%.

| card set | `close` decimals | distinct feature values | nn | line | beats | pair AUC | line | beats |
|---|---|---|---|---|---|---|---|---|
| `strict-flags` | [2] | 23 | 0.176471 | 0.166667 | YES | 0.605430 | 0.513303 | YES |
| `strict-flags-k1` | [3] | 126 | 0.215686 | 0.176471 | YES | 0.629749 | 0.512369 | YES |

## E-4 · the shuffle calibration, reviewed run `386d234b85269a21` against second-fix run `756cf4ea156d92c3`

Card-level and representative columns are unchanged in every row: True.

| configuration | predictor | card-level | block, reviewed (withdrawn) | block, second-fix | representative (n) |
|---|---|---|---|---|---|
| `none/none/none` | synthetic-iid | 0.5719 | 0.5588 | 0.5588 | 0.5654 (306) |
| `none/none/none` | synthetic-event-constant | 0.5719 | 0.5588 | 0.5588 | 0.5654 (306) |
| `start-hour/component/any` | synthetic-iid | 0.5719 | 0.5719 | 0.5523 | 0.5744 (289) |
| `start-hour/component/any` | synthetic-event-constant | 0.5654 | 0.5654 | 0.5588 | 0.5744 (289) |
| `start-hour/component/cross-coin` | synthetic-iid | 0.5719 | 0.5719 | 0.5523 | 0.5744 (289) |
| `start-hour/component/cross-coin` | synthetic-event-constant | 0.5654 | 0.5654 | 0.5588 | 0.5744 (289) |
| `move-window/component/any` | synthetic-iid | 0.5719 | 0.5654 | 0.5654 | 0.6031 (131) |
| `move-window/component/any` | synthetic-event-constant | 0.5621 | 0.5817 | 0.5948 | 0.6031 (131) |
| `move-window/component/cross-coin` | synthetic-iid | 0.5719 | 0.5654 | 0.5654 | 0.5882 (136) |
| `move-window/component/cross-coin` | synthetic-event-constant | 0.5654 | 0.5784 | 0.5980 | 0.5882 (136) |
| `move-window/greedy-clique/any` | synthetic-iid | 0.5719 | 0.5654 | 0.5654 | 0.5901 (161) |
| `move-window/greedy-clique/any` | synthetic-event-constant | 0.5588 | 0.5719 | 0.5980 | 0.5901 (161) |
| `move-window/greedy-clique/cross-coin` | synthetic-iid | 0.5719 | 0.5588 | 0.5588 | 0.5893 (168) |
| `move-window/greedy-clique/cross-coin` | synthetic-event-constant | 0.5621 | 0.5752 | 0.5752 | 0.5893 (168) |
| `card-span/component/any` | synthetic-iid | 0.5719 | 0.5654 | 0.5588 | 0.6552 (58) |
| `card-span/component/any` | synthetic-event-constant | 0.5686 | 0.5817 | 0.5621 | 0.6552 (58) |
| `card-span/component/cross-coin` | synthetic-iid | 0.5719 | 0.5654 | 0.5588 | 0.6613 (62) |
| `card-span/component/cross-coin` | synthetic-event-constant | 0.5654 | 0.5784 | 0.5523 | 0.6613 (62) |
| `card-span/greedy-clique/any` | synthetic-iid | 0.5719 | 0.5588 | 0.5523 | 0.6121 (116) |
| `card-span/greedy-clique/any` | synthetic-event-constant | 0.5621 | 0.5817 | 0.6013 | 0.6121 (116) |
| `card-span/greedy-clique/cross-coin` | synthetic-iid | 0.5719 | 0.5654 | 0.5458 | 0.6000 (125) |
| `card-span/greedy-clique/cross-coin` | synthetic-event-constant | 0.5654 | 0.5719 | 0.5719 | 0.6000 (125) |

Over the ten collapsed configurations and both predictors (20 rows): block minus card-level, reviewed function: -0.0131 to +0.0196; second-fix function: -0.0261 to +0.0392; representative minus card-level: +0.0025 to +0.0959.

Reference for the size of Monte Carlo noise: under `none/none/none` every event is one card, so the block shuffle and the card-level shuffle draw from the same null distribution; their two 1% boundaries, from the same seed, are 0.5588 and 0.5719.

