# Gate sensitivity — card set `blinded-strict-flags-unrounded`, run `7f6cd821a957440e`

Written by `scripts/27_gate_sensitivity.py` (criterion K-12). Feature subsets of the gate row, not renderings: no card was built. **Not for juror files.**

| field | value |
|---|---|
| run number (RULES 29) | `7f6cd821a957440e` |
| full input fingerprint | `7f6cd821a957440ec8ecba975890e769814035b6582da4cc71f8694828550cc1` |
| written at (system clock, UTC, RULES 23) | 2026-10-01T20:27:36Z |
| free disk space at start (bytes) | 12420096000 |
| card folder | `exam-prep/third-fix/blind-proof/strict-flags-unrounded/cards` |
| `scripts/16_identity_audit.py` SHA-256 | `4a248f78c78376c3b58ce7b02bc20af2c035e8089529449d303c70061164f4da` |
| `scripts/27_gate_sensitivity.py` SHA-256 | `e35c9f497c3d4143d6bff74dce6f0315a8648fffec14e5a915e72098f2169505` |

| variant | features | cards with a tied nearest neighbour | nearest neighbour (line) | tie-free nearest neighbour (line) | pair AUC (line) |
|---|---|---|---|---|---|
| (a) ALL-removable as audited | 26 | 0 | 0.238562 (0.176471) beats | 0.238562 (0.176471) beats | 0.545585 (0.513710) beats |
| (b) without the price-column families | 22 | 0 | 0.124183 (0.176471) no | 0.124183 (0.176471) no | 0.527217 (0.513604) beats |
| (c) as (b), and without the trade-count features | 17 | 0 | 0.137255 (0.173203) no | 0.137255 (0.173203) no | 0.529922 (0.514282) beats |

Features in each variant:

- (a) ALL-removable as audited: `gran-close:min_step`, `price:log_median_close`, `ratio:log_median_ls_acct`, `rep-close:close:distinct`, `rep-close:close:maxrepeat`, `rep-depth:depth +1%:distinct`, `rep-depth:depth +1%:maxrepeat`, `rep-depth:depth -1%:distinct`, `rep-depth:depth -1%:maxrepeat`, `rep-openint:open int:distinct`, `rep-openint:open int:maxrepeat`, `rep-ratio:L/S acct:distinct`, `rep-ratio:L/S acct:maxrepeat`, `rep-trades:trades:distinct`, `rep-trades:trades:maxrepeat`, `shape:acf1_log_depth_ask`, `shape:acf1_log_ls_acct`, `shape:acf1_log_taker_ls`, `shape:acf1_log_top_ls`, `shape:acf1_log_trades`, `shape:acf1_log_vol`, `shape:sd_log_depth_ask`, `shape:sd_log_depth_bid`, `shape:sd_log_ls_acct`, `shape:sd_log_trades`, `trades:log_median_trades`
- (b) without the price-column families: `ratio:log_median_ls_acct`, `rep-depth:depth +1%:distinct`, `rep-depth:depth +1%:maxrepeat`, `rep-depth:depth -1%:distinct`, `rep-depth:depth -1%:maxrepeat`, `rep-openint:open int:distinct`, `rep-openint:open int:maxrepeat`, `rep-ratio:L/S acct:distinct`, `rep-ratio:L/S acct:maxrepeat`, `rep-trades:trades:distinct`, `rep-trades:trades:maxrepeat`, `shape:acf1_log_depth_ask`, `shape:acf1_log_ls_acct`, `shape:acf1_log_taker_ls`, `shape:acf1_log_top_ls`, `shape:acf1_log_trades`, `shape:acf1_log_vol`, `shape:sd_log_depth_ask`, `shape:sd_log_depth_bid`, `shape:sd_log_ls_acct`, `shape:sd_log_trades`, `trades:log_median_trades`
- (c) as (b), and without the trade-count features: `ratio:log_median_ls_acct`, `rep-depth:depth +1%:distinct`, `rep-depth:depth +1%:maxrepeat`, `rep-depth:depth -1%:distinct`, `rep-depth:depth -1%:maxrepeat`, `rep-openint:open int:distinct`, `rep-openint:open int:maxrepeat`, `rep-ratio:L/S acct:distinct`, `rep-ratio:L/S acct:maxrepeat`, `shape:acf1_log_depth_ask`, `shape:acf1_log_ls_acct`, `shape:acf1_log_taker_ls`, `shape:acf1_log_top_ls`, `shape:acf1_log_vol`, `shape:sd_log_depth_ask`, `shape:sd_log_depth_bid`, `shape:sd_log_ls_acct`

