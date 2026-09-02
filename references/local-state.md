# Local State

Separate distribution, Session work, project learning, and global learner state by lifecycle.

## State home

Use the first available location:

1. non-empty `$XUNXUN_HOME`;
2. `~/.xunxun`.

This directory is private local state. Never place real learner state inside the Skill checkout or a project repository, and never commit, push, upload, or use it as telemetry.

If the state home is unreadable or unwritable, continue with Session-only adaptation. Do not block the explanation or pretend a durable update succeeded; disclose the limitation only when persistence becomes relevant.

## Layout

```text
<state-home>/
└── learners/
    └── <learner-id>/
        ├── profile.md
        ├── vocabulary.md
        └── projects/
            └── <project-key>.md
```

- `profile.md` — stable and contextual teaching preferences that apply across projects.
- `vocabulary.md` — cross-project vocabulary with demonstrated, domain-scoped evidence.
- `projects/<project-key>.md` — project route, progress, unresolved gaps, project/domain vocabulary, and project-scoped treatments.

Use the templates in `references/local-state-templates.md` when creating a missing file.

## Learner identity

Use an explicitly chosen learner id. A personal installation with exactly one existing learner may reuse it without asking. A fresh personal installation may use `default`; if multiple learner directories exist and the current learner is unclear, ask once which one to use.

Treat the learner id as a local label, not authentication. Reject `.`、`..`、path separators, and empty labels before using it in a path.

Never derive learner identity from a GitHub account, operating-system username, email, path, browser session, or repository metadata.

## Project key

For a Git repository with a canonical remote, derive a local filename-safe key from `host-owner-repository`, stripping protocol and `.git`, for example:

```text
https://github.com/deepseek-ai/deepseek-harness.git
  → github.com-deepseek-ai-deepseek-harness
```

For a project without a remote, use `local-<basename>`. If that key already names a different recorded canonical root, append a short local path fingerprint rather than merging the projects. Record the canonical remote or root inside the ledger so a collision is detectable.

Project identity never identifies the learner.

## Session lifecycle

The current Session is the active conversation or task. Its state is deliberately ephemeral:

- selected explanation preset;
- current learning route and exact position;
- terms introduced during this conversation;
- active low-confidence treatments and proximal predictions;
- immediate observations and unresolved ambiguity.

Do not create a per-Session file. Agent runtimes do not expose one portable stable Session id, and persisting every transient observation would create stale logs.

At a natural lesson milestone:

- write project route/progress and recurring project vocabulary to the project ledger;
- keep one-off introduced terms and weak treatment guesses ephemeral;
- use a promotion checkpoint before writing a consequential long-term learner preference;
- promote vocabulary globally only after cross-project or otherwise domain-general demonstrated use.

This is how continuity crosses Sessions: not by restoring an entire old conversation, but by loading the latest compact project checkpoint plus global preferences.

## Read precedence

For teaching preferences:

```text
current Session evidence
  > matching project-scoped preference/treatment
  > matching global profile preference
  > preset default
```

For terminology:

```text
current Session evidence
  > exact term@domain in project ledger
  > exact term@domain demonstrated in global vocabulary
  > unknown
```

An overloaded term must use a domain-qualified key, such as `context@cordis` and `context@react`. Evidence for one does not establish the other.

## Persistence inputs and outputs

Inputs to a persistence decision:

- learner id;
- optional project key and canonical root/remote;
- topic/domain;
- treatment or term;
- current Session evidence;
- intended scope: Session, project, or global;
- confidence and contradictory evidence.

Outputs are one of:

- no write — keep transient state in the Session;
- project checkpoint update;
- project vocabulary/treatment update;
- global profile promotion;
- global vocabulary promotion;
- downgrade, narrow, supersede, or remove an earlier conclusion.

Prefer an atomic file edit that preserves unrelated state. Never append raw transcripts. Consolidate repeated evidence into the existing treatment, term, route, or preference entry.

## What belongs where

| State | Session | Project ledger | Global profile/vocabulary |
|---|---|---|---|
| Current question and draft explanation | yes | no | no |
| Newly introduced incidental term | yes | usually no | no |
| Project route and next module | working copy | yes | no |
| Project-specific meaning, e.g. `service@cordis` | working copy | yes | only after broader demonstrated transfer |
| Active low-confidence treatment | yes | only if it must survive a Session | no |
| Stable pacing/representation preference | observed here | optional evidence | yes after promotion |
| Raw transcript or sensitive content | no persistence | no | no |

## Honest boundary

This is an instruction-driven Markdown store, not a database. Correctness depends on an Agent loading and updating the right files. There is no locking, schema enforcement, automatic Session-end hook, cross-device sync, or account service. If concurrent writers or machine synchronization become real requirements, add a dedicated state module then; do not simulate them with more Markdown rules.
