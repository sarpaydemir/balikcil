# Fingerprints — second-fix run

Mateo · data engineer · taken from the system clock at 2026-10-01T19:30:05Z (RULES 23).

This file does not list itself; its SHA-256 is in the run's report to the coordinator.

## Instruments

| script | as reviewed (REVIEW §8, commit `7735d08`) | now |
|---|---|---|
| `scripts/lab_cards.py` | `96b0eb01c502a40b4e76c864681763206ba627b268eedb7eb19984f81d9b928e` | `96b0eb01c502a40b4e76c864681763206ba627b268eedb7eb19984f81d9b928e` (unchanged) |
| `scripts/15_event_collapse.py` | `f3de235883aac8b364aa5391c8371d50a9ecca288007f8d0bfaadadafe0ffb12` | `a0bcc6001fd8a884211b9e3b90102a02037db8959fb7776166d50735e2f68280` |
| `scripts/16_identity_audit.py` | `4c4928b84ff9b484995058c2dd4e5b043af1491b60f314e1a0f418dd90e4a371` | `4dfd9fd12de458e499ceeea88d9f445d10f853fd21ccb22dc407185a5b767a91` |
| `scripts/17_blind_cards.py` | `ee064204016f110d18ceb4feda2c6f6f8c3c78ce97a0cf7d3f34e225f86f9515` | `b2853b66580130121c149b9b8c6eef2ba2c50b2e4c2c5d1bc5d31f552bb0dbed` |
| `scripts/18_residual_diagnostic.py` | `52ebb0a115656fad7341ec22db1d98859b48a09788e1c306118ff472ecda2015` | `9db9f7b06cb773fe269603882576f01a89af8ac092ed01773cbc63cbf4acb429` |
| `scripts/24_review_checks.py` | — (new) | `de072d80820344a7ad6f73980fb99cfb0e0c5d129e6f8682bc6b06e50909f14c` |
| `scripts/25_instrument_checks.py` | — (new) | `08bf00f6650ce7a4e08862860ffe17ba43e41448e4df855077acc01f820f6863` |

## Earlier files with an appended addendum

Each keeps its earlier bytes; the check hashes exactly the earlier length.

| file | earlier length (bytes) | earlier SHA-256 | leading bytes now hash to | current SHA-256 |
|---|---|---|---|---|
| `exam-prep/VERDICT.md` | 5512 | `c5bd5532615ee28fc3016ba2cc07246b428c5d19dcb8b580df5d5752ccb96cf0` | `c5bd5532615ee28fc3016ba2cc07246b428c5d19dcb8b580df5d5752ccb96cf0` (match) | `d83c2b85fe8548634193fa60d8c98e090559b7211f6066b21727a4482835fab5` |
| `exam-prep/R-04-blindness.md` | 19807 | `c20f9c5b6ea5ed6900eade6f844b01b2fca06db98dd9862dbda239d4e4b731d7` | `c20f9c5b6ea5ed6900eade6f844b01b2fca06db98dd9862dbda239d4e4b731d7` (match) | `64cde9b7f197143361fee1b061913304ac51814f1f9d302c852828ccbd316354` |
| `exam-prep/N-1-collapse.md` | 12755 | `28baee9ca7928755fed3c2a860eb05a8111cf4a543c46c349b17a9422fa9899b` | `28baee9ca7928755fed3c2a860eb05a8111cf4a543c46c349b17a9422fa9899b` (match) | `7dee08bd1e53e0f20c2c992f784241361b5df6716fbeff1f9ee637f64727c50e` |
| `exam-prep/decisions-and-open-questions.md` | 9332 | `9abd49462f5c33d912250f101822934b4028be85cf02c95328e506b672db4538` | `9abd49462f5c33d912250f101822934b4028be85cf02c95328e506b672db4538` (match) | `6d7f31814538b65795fc9d3afd06b90f5aa383d69af2a5b9b7619a7df6692801` |
| `exam-prep/README.md` | 3068 | `d315670d9b6cfc66f9e9551d54ba4c7a82dcef46cb307cfeba586b8ac66fcd3f` | `d315670d9b6cfc66f9e9551d54ba4c7a82dcef46cb307cfeba586b8ac66fcd3f` (match) | `c704496b8234ac6d397ad50f7ea9f8d064dbc41ba5500b7d80173e9125f9d375` |
| `exam-prep/FINGERPRINTS.md` | 8006 | `06ce674f2c051929a341105c76cce36c1ef1723eeeb876e109e25303c0dffad7` | `06ce674f2c051929a341105c76cce36c1ef1723eeeb876e109e25303c0dffad7` (match) | `22af15455f276d7cc20005a30718466fd1160dbee81ab9c0b79351a8211c0c3b` |

`exam-prep/REVIEW.md` is unchanged: `3697d5f5a60c57349950adebef5f9ac45c6691a1001638eb37a49cea8d6af7e0`.

## Files written by this run

| file | SHA-256 |
|---|---|
| `exam-prep/JUROR-QUESTIONS.md` | `7020127c257b7addbae1fd6cbca0e4031accc3b28a4816980c5cd410532399d9` |
| `exam-prep/collapse/run-756cf4ea156d92c3/collapse-manifest.md` | `2e8c2dcc512699f05d092309383976df288234b376afdf420f27a8078ceaa383` |
| `exam-prep/collapse/run-756cf4ea156d92c3/collapse-manifest.md.sha256` | `f0806877579348bc0f2a1940b2e808c2ed19aab9b0dfebcb2ada61a9afa1ea2e` |
| `exam-prep/collapse/run-756cf4ea156d92c3/collapse-summary.csv` | `94d9205c77918551b4fbe0df9806abdf14d0599ae96ed911553e446652676bcd` |
| `exam-prep/collapse/run-756cf4ea156d92c3/events.csv` | `7d887b831847b8838735ec0db334238cda51d9709ec6d7c97a1aa12f1faba727` |
| `exam-prep/collapse/run-756cf4ea156d92c3/shuffle-calibration.csv` | `0c4b27f9556086644ff5ad9137322a06854f64b78daf9bf1babebd73115b5cd7` |
| `exam-prep/collapse/runs/756cf4ea156d92c3.json` | `e426081948fb99292fa892c89695b2f769378f8c7420af0eca95b73ec98ed32c` |
| `exam-prep/second-fix/SECOND-FIX.md` | `40cc4b7601f33b9066747e408a1e76624c15b4d34422dc41e800ffce5a3494a7` |
| `exam-prep/second-fix/blind-proof/strict-flags-k1/blind-manifest-strict-flags-k1.md` | `204dd27637bb84ed4626bfaeb0eb6cc1307f612af9a3a8fb5368db3fc8a7b06f` |
| `exam-prep/second-fix/blind-proof/strict-flags-k1/runs/151e6ccdc930d4b4.json` | `68132711d59e45cb79066f7eb31fd9070b04747f382fb75f21f977438111cd19` |
| `exam-prep/second-fix/blind-proof/strict-flags-k1/truth-strict-flags-k1.csv` | `02546086447ddf4bbdcb0e224e1b672a5fa7986dfabe2de0174b5063190a4e13` |
| `exam-prep/second-fix/checks/instrument-checks-35925ca8acf60690.md` | `9a237be49c4f7b228cea5ef6b35cffc2b9e202beade8093ad455a8c963af3204` |
| `exam-prep/second-fix/checks/review-checks-28b29921e160d204.md` | `14b473506c02713f28ed0ee962f29822ca7b057a405784a6b6f42aba976398ca` |
| `exam-prep/second-fix/checks/runs/28b29921e160d204.json` | `62e6f92459c5d150e847adff31307a8826e5005556c7d969d7828ed576358a8b` |
| `exam-prep/second-fix/checks/runs/35925ca8acf60690.json` | `48813e54847317807ef054d05030513d06be6a81627d8a294ec2a3790c37ed19` |
| `exam-prep/second-fix/criteria-written-before-measuring.md` | `0613f693144dcb6455c1b150500de942a3cf2d0479c315b7c4823c568913906a` |
| `exam-prep/second-fix/identity/run-13d935bb5cf78346/hour-linkage-raw-observation.csv` | `d591bebacbb18592695509c08d2da0861d9ec1a2ff2a3d6020aad31e6484facd` |
| `exam-prep/second-fix/identity/run-13d935bb5cf78346/identity-audit-raw-observation.csv` | `2bfa60be6993836d39405feb89e56abed3b05cfca9fb02ea76f3d8b75c67f6e7` |
| `exam-prep/second-fix/identity/run-13d935bb5cf78346/identity-audit-raw-observation.md` | `af7096bc4282a5e4c15ad9d08be213d55ab592f5743a0d6f33ac49f1fbb9337e` |
| `exam-prep/second-fix/identity/run-4a33cb19150e9718/hour-linkage-blinded-strict-flags-k1.csv` | `841a8236190c38b4737845fc794f65f2c21e4b80b511fb8a4aba7e932a1222e2` |
| `exam-prep/second-fix/identity/run-4a33cb19150e9718/identity-audit-blinded-strict-flags-k1.csv` | `e54f4b92bad360e0f1777bdc67a96ce671150eac5090e58bf8882530572eafd4` |
| `exam-prep/second-fix/identity/run-4a33cb19150e9718/identity-audit-blinded-strict-flags-k1.md` | `bf905c717e201a511c21e328882f1ed7b1881945036dd5af6116473d106cae6b` |
| `exam-prep/second-fix/identity/run-5fce3f6fbe815bae/hour-linkage-blinded-rank.csv` | `11f07aa54741e567e5235796b761959e8b662ae2570ac79f36c2b69088386b50` |
| `exam-prep/second-fix/identity/run-5fce3f6fbe815bae/identity-audit-blinded-rank.csv` | `a90d32ebf5fc26018ac1f827df50efe82df3d66fe0197acd397356c7f5f4156e` |
| `exam-prep/second-fix/identity/run-5fce3f6fbe815bae/identity-audit-blinded-rank.md` | `d47d007f031831715f629ef362590231399ce6f7c9524544e3c71cd6678b69d4` |
| `exam-prep/second-fix/identity/run-6f3cffc734151ae1/residual-diagnostic-blinded-strict-flags.md` | `456adbe985ba88f3f95e2229ac14947a870f7cd1ace006271d9890f6887f7f70` |
| `exam-prep/second-fix/identity/run-7173272492382a51/hour-linkage-blinded-strict.csv` | `b375bfa33904921336f8ddc5caba2dbb72f80a256adfd6f3d8087164d8a59ce1` |
| `exam-prep/second-fix/identity/run-7173272492382a51/identity-audit-blinded-strict.csv` | `31ff73ce546224e7a6d476c1e8ff48af740f5fcde657d0b8195e894ccee51038` |
| `exam-prep/second-fix/identity/run-7173272492382a51/identity-audit-blinded-strict.md` | `f6188fc67ffb36a0bbb78c20ce6e68a75656d0f0d0fbe8c560316ee2776732c1` |
| `exam-prep/second-fix/identity/run-9cdd61c13254bc69/residual-diagnostic-blinded-strict-flags-k1.md` | `edbff7cfb2b176075bd8e33f5877af30a0b96bff7793505f062f0f7e979360be` |
| `exam-prep/second-fix/identity/run-d70dd7b545bfce8a/hour-linkage-blinded-strict-flags.csv` | `3f7f32110838f8210d5767eb51aaadd9854288b7e6b4c03da2903571773f0bf9` |
| `exam-prep/second-fix/identity/run-d70dd7b545bfce8a/identity-audit-blinded-strict-flags.csv` | `851fdced49c0b1bca41dd73248c260cf24bad11cde2f38e2e60e0b1bdc91c4bb` |
| `exam-prep/second-fix/identity/run-d70dd7b545bfce8a/identity-audit-blinded-strict-flags.md` | `f2e30a6b0ae0ff585a45a6d142594508f367f49058efbda4749e0bba1695ead1` |
| `exam-prep/second-fix/identity/run-d91cfc33459a0270/hour-linkage-blinded-ratio.csv` | `c0f739f843f0dedd636328d5febaa9adc0a81ffd1f410da9e75ac8e73eddbe33` |
| `exam-prep/second-fix/identity/run-d91cfc33459a0270/identity-audit-blinded-ratio.csv` | `bb8249b6ba2b1704cdf37d804b6b988e82b7d16feead102a0f79b40c31e0c7ed` |
| `exam-prep/second-fix/identity/run-d91cfc33459a0270/identity-audit-blinded-ratio.md` | `7a309f446a1f3dc5db11efa67962c16a79d2113d328a35ddc0f1b799d20bc3a1` |
| `exam-prep/second-fix/identity/runs/13d935bb5cf78346.json` | `d0a686962784fc5d96ebffff118994aa73a8b6bd7462e37121689a62d6998815` |
| `exam-prep/second-fix/identity/runs/4a33cb19150e9718.json` | `eea304f41d025bc316657d3a285401a025b9b02dee3ddd9d68546b1ac6928d42` |
| `exam-prep/second-fix/identity/runs/5fce3f6fbe815bae.json` | `8631661c04ae676c08bf319ffd191b9375960f3a2ff3ae4a838a0a59dc5d97e5` |
| `exam-prep/second-fix/identity/runs/6f3cffc734151ae1.json` | `845cc8d04f05d3f143c961f17b3f82da4b2a99a92c4999cbefc50e9021d2284c` |
| `exam-prep/second-fix/identity/runs/7173272492382a51.json` | `92d3aa46559c30dedf8e3a12f3083968c1d9201bca03727ebfa88077185937e7` |
| `exam-prep/second-fix/identity/runs/9cdd61c13254bc69.json` | `3591f091b010ea844314480f07fb7d62a8380ce9926d7847a094e115b546715e` |
| `exam-prep/second-fix/identity/runs/d70dd7b545bfce8a.json` | `aab5b26fe8c685e319e7a251014c8fb5bd56db2faa1f530af3130c952736bf64` |
| `exam-prep/second-fix/identity/runs/d91cfc33459a0270.json` | `af147fb24bd177ffeb0a89893e62cef6090754e03eb05e811649750571459a44` |
| `exam-prep/second-fix/juror-questions/JQ-B1.md` | `6e534b3564124cf948ce0e74e2d84b4337ac652a915d4778248757aaf7986c60` |
| `exam-prep/second-fix/juror-questions/JQ-N1.md` | `dd78af5b108964368174356744314bfe0d17156a38dd92dc9ad7acf7d6660511` |
| `exam-prep/second-fix/juror-questions/JQ-R04-CONTENT.md` | `857bcfa26a6ba9bac0607a5709b54a8ceeece522f271bf34e20d6aca1c8bff30` |
| `exam-prep/second-fix/juror-questions/JQ-R04-DATE.md` | `771709e40067cac25fc40882fdb19c0b29da90876bd3a57977630e07baa189b0` |
| `exam-prep/second-fix/juror-questions/JQ-R04-GATE.md` | `e8000bb9790f991f1fd1bf7b3b8768dd326cfd3011ebb1990131b70fb69787ed` |
| `exam-prep/second-fix/logs/run-audits.log` | `6c897cb7b37808e5965e684ad7b2f8e77c23a471f127bb557c13912e90149946` |
| `exam-prep/second-fix/logs/run-audits.sh` | `d9d059b01e631a94de26d69940f0a578fa230de5f4f5ba95372b0db257184860` |

The 306 blinded cards in `exam-prep/second-fix/blind-proof/strict-flags-k1/cards/`, combined (SHA-256 over the concatenation, in card-id order, of `<id>:<SHA-256 of card file>\n`): `ffda9e30f02724a2958e4ec604a8d66c205d804f3f9082886f7ee903d44eb492`.

## Run numbers (RULES 29)

| run | script | what |
|---|---|---|
| `28b29921e160d204` | `24_review_checks.py` | re-measurement of every review number, against the reviewed code |
| `756cf4ea156d92c3` | `15_event_collapse.py` | collapse engine with the repaired block shuffle |
| `151e6ccdc930d4b4` | `17_blind_cards.py` | blinded set `strict-flags-k1` (K-1) |
| `13d935bb5cf78346` | `16_identity_audit.py` | extended audit, raw observation cards |
| `d91cfc33459a0270` | `16_identity_audit.py` | extended audit, `ratio` |
| `5fce3f6fbe815bae` | `16_identity_audit.py` | extended audit, `rank` |
| `7173272492382a51` | `16_identity_audit.py` | extended audit, `strict` |
| `d70dd7b545bfce8a` | `16_identity_audit.py` | extended audit, `strict-flags` |
| `4a33cb19150e9718` | `16_identity_audit.py` | extended audit, `strict-flags-k1` |
| `6f3cffc734151ae1` | `18_residual_diagnostic.py` | residual diagnostic, `strict-flags`, extended features |
| `9cdd61c13254bc69` | `18_residual_diagnostic.py` | residual diagnostic, `strict-flags-k1`, extended features |
| `35925ca8acf60690` | `25_instrument_checks.py` | regression, engine guards, K-4 probe, calibration comparison |

Re-running `15`, `16` (on `strict-flags`) and `25` with the same inputs reported "already recorded … nothing written" (RULES 29–30); checked once, after the runs above and before the documents were written.
