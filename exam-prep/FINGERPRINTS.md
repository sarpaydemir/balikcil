# Fingerprints — `exam-prep/` and the instruments

Mateo · data engineer · taken from the system clock at 2026-09-19T14:19:30Z (RULES 23).

The 1,224 blinded card files in `blind-proof/*/cards/` are not listed one by one; each variant's combined fingerprint is in `R-04-blindness.md` §10 and in that variant's run record.

A manifest carries the time it was written, so re-running a script rewrites its manifest with a new timestamp even though the **run number** — the fingerprint of the inputs, RULES 29 — is unchanged. The run numbers in `runs/` are the stable identity; these hashes identify the exact text of the documents.

## Scripts

| file | SHA-256 |
|---|---|
| `scripts/lab_cards.py` | `96b0eb01c502a40b4e76c864681763206ba627b268eedb7eb19984f81d9b928e` |
| `scripts/15_event_collapse.py` | `f3de235883aac8b364aa5391c8371d50a9ecca288007f8d0bfaadadafe0ffb12` |
| `scripts/16_identity_audit.py` | `4c4928b84ff9b484995058c2dd4e5b043af1491b60f314e1a0f418dd90e4a371` |
| `scripts/17_blind_cards.py` | `ee064204016f110d18ceb4feda2c6f6f8c3c78ce97a0cf7d3f34e225f86f9515` |
| `scripts/18_residual_diagnostic.py` | `52ebb0a115656fad7341ec22db1d98859b48a09788e1c306118ff472ecda2015` |

## `exam-prep/`

| file | SHA-256 |
|---|---|
| `exam-prep/blind-proof/rank/blind-manifest-rank.md` | `2b8cf4b092a5e281ee28c079e9c57a904fb639f08c549bbee8dbb56e6a6b9276` |
| `exam-prep/blind-proof/rank/runs/35df01d621d8da5a.json` | `7ff9e8b900ae209f86f4ff187981934edaf24c4cb51ab222ff0ccd67bc68cfb5` |
| `exam-prep/blind-proof/rank/runs/a428c67e72db2315.json` | `3121c20df5719357fa8a5ba959f20dc98d6460543fe785e3fcc9609d68e431a7` |
| `exam-prep/blind-proof/rank/truth-rank.csv` | `02546086447ddf4bbdcb0e224e1b672a5fa7986dfabe2de0174b5063190a4e13` |
| `exam-prep/blind-proof/ratio/blind-manifest-ratio.md` | `3e38ec0004089b4d5eab9313c1f071b359675c2380e24494c1eae4a2653852e8` |
| `exam-prep/blind-proof/ratio/runs/ca9e460829ecdac5.json` | `812db10ca4b88d7421ed48763bafb1a048e54629a99a799f07984280c3ef1b14` |
| `exam-prep/blind-proof/ratio/runs/ea2a67abf083210a.json` | `a5698a59c81a3ca840ed966c5ec1968792e046e48cc7a3691084c3e743edd333` |
| `exam-prep/blind-proof/ratio/truth-ratio.csv` | `02546086447ddf4bbdcb0e224e1b672a5fa7986dfabe2de0174b5063190a4e13` |
| `exam-prep/blind-proof/strict/blind-manifest-strict.md` | `60a6872775ebc735a75c73a3ec74ff1fa025438304cd87108f15db2c87b0ac20` |
| `exam-prep/blind-proof/strict-flags/blind-manifest-strict-flags.md` | `6dcfeba3a70db2d35384e29b603fc5f87b14bb7d147cdbd0fe020040e9d24e5a` |
| `exam-prep/blind-proof/strict-flags/runs/10405ae115941d40.json` | `be2e0e020aa069ae80c9354cfeff94b68b219be950c6411dad61fc1593ad1d9e` |
| `exam-prep/blind-proof/strict-flags/truth-strict-flags.csv` | `02546086447ddf4bbdcb0e224e1b672a5fa7986dfabe2de0174b5063190a4e13` |
| `exam-prep/blind-proof/strict/runs/97c22213917ba4f2.json` | `80025a08192c2dde1813b966d15005e08e8f5a17dcc261704f5e0fef78f574e2` |
| `exam-prep/blind-proof/strict/runs/a9a8f3bcd515fd62.json` | `c88ad792214000340ffbe8166f461d81199bcadb4f62218b9581981bb7245df6` |
| `exam-prep/blind-proof/strict/truth-strict.csv` | `02546086447ddf4bbdcb0e224e1b672a5fa7986dfabe2de0174b5063190a4e13` |
| `exam-prep/collapse/collapse-manifest.md` | `1d7a6a8e64e492ccea261ed3ea32bb3cb432a30b0c359c6d3092b493d450fc89` |
| `exam-prep/collapse/collapse-manifest.md.sha256` | `45b703a0430932ca9086d4664af85e454ab6b6c849d63ea42f10865ee35a7a99` |
| `exam-prep/collapse/collapse-summary.csv` | `6f3f5ce5748fc5e9d95086d07bbd6f7db9b00539b1df4445463a2df01f1400f5` |
| `exam-prep/collapse/events.csv` | `7d887b831847b8838735ec0db334238cda51d9709ec6d7c97a1aa12f1faba727` |
| `exam-prep/collapse/runs/386d234b85269a21.json` | `f22bc5663154f93995652b419d32483e25fc1fb584a74387b09ef109ce67f195` |
| `exam-prep/collapse/runs/4af3b344a4898af0.json` | `f6eace00d7a571ffdfac4693441143a1c5d0a82461d74714fe4d265e8b6419d5` |
| `exam-prep/collapse/runs/5ba9140fe3c467fa.json` | `70d27ae9a2a98656b6555e57c63586263b573270885c04dfdcb5da32e90863f6` |
| `exam-prep/collapse/shuffle-calibration.csv` | `145069adbb97faae4533c98bd009e7163200588942a5f57956a7eaf1981a6a66` |
| `exam-prep/decisions-and-open-questions.md` | `9abd49462f5c33d912250f101822934b4028be85cf02c95328e506b672db4538` |
| `exam-prep/identity/hour-linkage-blinded-rank.csv` | `4ebba376b70d226d47bae572feff87a5dc4be658b3f5e0381b22ef7a75c4fa01` |
| `exam-prep/identity/hour-linkage-blinded-ratio.csv` | `6cc5dd02ac6a7f824addd22290b69414715c74757d9d9fbcc4f96c812f56302b` |
| `exam-prep/identity/hour-linkage-blinded-strict.csv` | `31744f099320b07d78caec0849a7e4604216a4f8fea8f30af94ed79785c6d495` |
| `exam-prep/identity/hour-linkage-blinded-strict-flags.csv` | `1a9ed2c1f5a13d4993f8a8a50330cc8dd1f507cbe5450c98fd3edc100622ce9e` |
| `exam-prep/identity/hour-linkage-raw-observation.csv` | `967458ff6a1b390bd2c8bdc2d338f179095e255776432092bdd033456d13ea59` |
| `exam-prep/identity/identity-audit-blinded-rank.csv` | `4b24272ad07cfa0bde6d23925d4f10aa3947642a475d9c35a49482b89fca2c5c` |
| `exam-prep/identity/identity-audit-blinded-rank.md` | `7bdefadc856a62ef09ec529887be03587a0e9d624acfe89bdbc0be0d209b0e9c` |
| `exam-prep/identity/identity-audit-blinded-ratio.csv` | `693442d4f6cf69b293797ee904adf302654e2b4b426048d9762e0aaf5f7610e2` |
| `exam-prep/identity/identity-audit-blinded-ratio.md` | `25ecd63a6f32a0b8c911d4cbe8df965a51650cf347d2bd0a5e7a1fbec092b148` |
| `exam-prep/identity/identity-audit-blinded-strict.csv` | `69677b422ca21ca2991cefa7459ce343bc5f5803dbf4838f3c1e0f0f740b8586` |
| `exam-prep/identity/identity-audit-blinded-strict-flags.csv` | `e956446e19b34547cb6e03eb24de2b49ce172de799d489f93c00390ed8795143` |
| `exam-prep/identity/identity-audit-blinded-strict-flags.md` | `f51607da900a7c245f69e1c69dd8e6a0c45b6022aec08338bb4796951ddfdfad` |
| `exam-prep/identity/identity-audit-blinded-strict.md` | `76c2a58a4df92ba639b79a4ba417e301d56c741984548b20efe6c63919b1ed31` |
| `exam-prep/identity/identity-audit-raw-observation.csv` | `904b51057baf1cde00ea0ecab5d2627f4da5c2ed0c507ec294169782f828ad7c` |
| `exam-prep/identity/identity-audit-raw-observation.md` | `dca438fdde57fd74b1073fbf674a6ad17acb9f398a26990e63aef7a7927591da` |
| `exam-prep/identity/residual-diagnostic-blinded-strict-flags.md` | `c33251a953c8e7175d23305871b7198dc651fd01f0653679f2d04226590a6c94` |
| `exam-prep/identity/runs/07545d812086c68e.json` | `5acfc1f64d04def0f98430cf32d93de87772ecdab89784792e06f8d8340f82b4` |
| `exam-prep/identity/runs/0c56eac4f6270964.json` | `162c5aa40e70012b23e1e5986757bb2b66263f355fa0ac22d6d4025a3608ac4e` |
| `exam-prep/identity/runs/23502d75682cc455.json` | `44f37f01815f3dc7c1fa53fb14392bc4843ae127bfe2cdc4d32886f88935167c` |
| `exam-prep/identity/runs/364cdbe6a67680fe.json` | `e410db620a059c10be8bc11748577627f6a8578a3fb15584ea535790f7b22c22` |
| `exam-prep/identity/runs/39d37cc651d44526.json` | `a671f9d1b1a67e55c7fc4ed532e118630f703b1a2e4427b52f2ae70b4c84cf4c` |
| `exam-prep/identity/runs/3b1cb7d540d11283.json` | `62f21f7a7289ff750f0f745909de32a1b84d025e7e7f12014b38ab4bd54195f7` |
| `exam-prep/identity/runs/3c090e41041104e0.json` | `0182688d5f6e40fa94ba0b823367c5f48e35c47703f24b644adae3cd3a0612f2` |
| `exam-prep/identity/runs/8467e84647b325c8.json` | `2b7892f3cf864e3aac497c9c65627b6145f179684267612115cc5ae173e68877` |
| `exam-prep/identity/runs/b8230e324e0c03e6.json` | `df336146aaff72670088158a9b60335d318682fd7ddf291377f0d257f3891998` |
| `exam-prep/identity/runs/ba8d6b5e3880f9ee.json` | `3fb27373c6c7350c045e5b777fcaad85ebe7224f63619d9e4d78e314c70c4558` |
| `exam-prep/identity/runs/ca8b0bc394468298.json` | `8e92075b2682071527a5370aadfdc7cbd7f5198fe3ff4769ff29f62a6aa1d2c3` |
| `exam-prep/N-1-collapse.md` | `28baee9ca7928755fed3c2a860eb05a8111cf4a543c46c349b17a9422fa9899b` |
| `exam-prep/R-04-blindness.md` | `c20f9c5b6ea5ed6900eade6f844b01b2fca06db98dd9862dbda239d4e4b731d7` |
| `exam-prep/README.md` | `d315670d9b6cfc66f9e9551d54ba4c7a82dcef46cb307cfeba586b8ac66fcd3f` |
| `exam-prep/VERDICT.md` | `c5bd5532615ee28fc3016ba2cc07246b428c5d19dcb8b580df5d5752ccb96cf0` |
