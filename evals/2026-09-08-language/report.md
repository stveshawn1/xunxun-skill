# Response-language follow-up

The v3 English return-to-code question received Chinese answers under full Xunxun guidance in both repeats. A short rule now explicitly follows the requested response language, or otherwise the latest substantive user message.

The follow-up used the same GPT-6 Astra model, reasoning setting, tool prohibition, evidence and runner as v3. The only before/after difference was that rule. Each input was repeated twice per version.

| Input | Before: correct language | After: correct language |
|---|---:|---:|
| English continuation | 0/2 | 2/2 |
| Same English continuation, explicitly requesting Chinese | 2/2 | 2/2 |
| Chinese continuation | 2/2 | 2/2 |

All 12 calls completed successfully. The automated Han-character check described in the [protocol](protocol.md) matched inspection of the responses. These results support this narrow fix on the tested inputs. They do not prove reliable language choice for all multilingual conversations, or a broader teaching benefit.

## Evidence

- [Input messages](suite.json)
- [Frozen before guidance](guidance-before.txt)
- [Frozen after guidance](guidance-after.txt)
- [Raw answers](answers/)
- [Run metadata and hashes](runs.json)
- [Runnable language and hash check](check.py): `python3 evals/2026-09-08-language/check.py`
- Generation reused the v3 runner's `subject` function, with this directory as its output root. The supplied guidance is the complete frozen text, including references.

The language case was selected after observing the v3 failure; it is a targeted regression check, not a held-out generalization test.
