# Run Metadata

## Frozen inputs

- Skill under test: Xunxun content last changed at `ad434f7`; repository HEAD during scored runs was `fc0dc18`.
- Protocol was committed before generation at `67d617e`; the Skill-loading allowance was clarified before generation at `fc0dc18`.
- Codex CLI: `0.151.0-alpha.7.2`.
- Subject model: `gpt-5.6-sol`, reasoning effort `high`.
- Both conditions used the same empty working directory and source prompt bytes.
- `$XUNXUN_HOME` pointed to an isolated directory containing an empty `profile.md`; no project profile existed.

Prompt SHA-256:

| Case | SHA-256 |
|---|---|
| Pi Coding Agent | `9e97fa56efba277eee7a1ac5e1b6eb7ad6c0c678f4c3296b1174ea6b26686ad1` |
| OpenAI Agents SDK | `79d5511efdea3da436428856ce438c545380d874affe4f28ce54a32251375206` |
| DSH | `f3100133e0ee19608bef97873a62c8373cca36b61e553f5bab2a23ac41455541` |
| Adaptive immunity | `d944521728738d24ba558b46f2a5cd2bbadefb75893aa5fe433b4b5e29b5212a` |
| Financial statements | `2a43049348a0df1258061cff52164afae0cd58c23bf53b29a6d979be4e2ddcdc` |

## Isolation diagnostic

With identical CLI settings, the Baseline reported every ordinary visible Skill except `xunxun`; Treatment reported the same list plus `xunxun`. The Baseline used:

```text
-c 'skills.config=[{path="<xunxun-skill>/SKILL.md",enabled=false}]'
```

Both conditions otherwise used:

```text
codex exec --ephemeral --ignore-user-config --ignore-rules \
  --skip-git-repo-check -s read-only -m gpt-5.6-sol \
  -c 'model_reasoning_effort="high"' --color never --json
```

## Scored subject runs

| Run | Case | Condition | Selected Skill | Input tokens | Output tokens | Reasoning tokens |
|---|---|---|---|---:|---:|---:|
| P-B | Pi | Baseline | none | 15,761 | 909 | 226 |
| P-X | Pi | Xunxun | Xunxun | 52,338 | 1,467 | 492 |
| O-B | Agents SDK | Baseline | OpenAI Docs | 33,112 | 1,091 | 307 |
| O-X | Agents SDK | Xunxun | Xunxun | 52,713 | 1,539 | 503 |
| D-B | DSH | Baseline | none | 15,984 | 845 | 40 |
| D-X | DSH | Xunxun | Xunxun | 53,102 | 1,545 | 487 |
| I-B | Immunity | Baseline | none | 15,777 | 665 | 37 |
| I-X | Immunity | Xunxun | Xunxun | 52,482 | 1,538 | 532 |
| F-B | Accounting | Baseline | none | 15,836 | 688 | 119 |
| F-X | Accounting | Xunxun | Xunxun | 53,244 | 1,605 | 724 |

Token counts are cumulative runner-reported usage. Treatment normally required additional model turns to read `SKILL.md` and `presets.md`, so they measure execution overhead as well as final generation.

Every scored run exhausted five WebSocket retries and then succeeded through the CLI's HTTPS fallback. Because both arms showed the same transport pattern, this is recorded as shared environment noise rather than a quality signal.

## Invalid attempt

The first adaptive-immunity pair was excluded before scoring. Its Treatment incorrectly fell back from the intentionally empty `$XUNXUN_HOME` directory to the maintainer's real `~/.xunxun/profile.md`, contaminating the neutral-profile condition.

The isolated directory was given an explicit empty `profile.md`, then the whole pair was rerun. No output from the invalid pair appears in the scored files.

## Blinding and judges

Mapping was determined from the first hexadecimal character of `SHA-256("fc0dc18:" + case-id)`: odd means A=Xunxun, even means A=Baseline.

| Case | A | B |
|---|---|---|
| Pi Coding Agent | Xunxun | Baseline |
| OpenAI Agents SDK | Xunxun | Baseline |
| DSH | Baseline | Xunxun |
| Adaptive immunity | Baseline | Xunxun |
| Financial statements | Baseline | Xunxun |

The exact blinded judge input was 43,121 bytes with SHA-256 `b9213a26ac7ccc1d0d48bb0f1e82d06c2c53946ce88c390e575c5a77a201bde9`.

| Judge | Model | Input tokens | Output tokens | Reasoning tokens |
|---|---|---:|---:|---:|
| Sol | `gpt-5.6-sol`, high | 26,056 | 2,563 | 1,394 |
| Terra | `gpt-5.6-terra`, high | 26,056 | 2,324 | 1,445 |

Both judges had Xunxun disabled and returned JSON constrained by [`judges/schema.json`](judges/schema.json).

## Output integrity

| File | SHA-256 |
|---|---|
| `pi-coding-agent/baseline.md` | `b8d2f7731e621658c525337dbea5fd8a8947a5f686890eef2aaea8bcef7b8b8b` |
| `pi-coding-agent/xunxun.md` | `16e06c0dfd0a817f00a8fe84686c755e289c7ddb4ef9a7b14641ee97da537205` |
| `openai-agents-sdk/baseline.md` | `e0e9bff369b221d1220953f2bef756e161b72a4c2c870942b7c51aa33a063fa6` |
| `openai-agents-sdk/xunxun.md` | `805f0be4b2cc8fe5fcab9cbbf9fae34f8a01fb7e3f5c117cd311c5a296b898a6` |
| `dsh/baseline.md` | `e3c2d19898d609c2b4b0e35ccec060323b661bdf80b3c11040dcb62b72d5ca13` |
| `dsh/xunxun.md` | `d3c8e8ed3c73f04fae56644a888df6a24b2d5268d3330e3049709a1c5c438ba6` |
| `adaptive-immunity/baseline.md` | `1bc760a978a3695761de7b90894136009be71832818302d95955040ce0a3328c` |
| `adaptive-immunity/xunxun.md` | `3830aed7621477714d71ae290f33298e4183939b5bb4311e78465fc7aaa4a51c` |
| `financial-statements/baseline.md` | `cfaa88d3a6a46a9007168114f86fcd7e9c614dead249393096ab5a98259bf871` |
| `financial-statements/xunxun.md` | `8cee2a446ce94a82895feb5a8a299c1a7c48cf47ab105e625cd7952ddd13b607` |
| `judges/sol.json` | `c6a948491c7da23d25729fd44e53a1b3872dbf68ea06a7d908fe46645d84d7f9` |
| `judges/terra.json` | `52fb0d001b34761b5dd5bceb9e65a6b0f004186b411e89019def5aa901342042` |
