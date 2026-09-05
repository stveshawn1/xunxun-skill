# Local State

Separate learning state by scope and lifecycle without building a vocabulary database.

## Layout

```text
~/.xunxun/
└── profile.md                  # cross-project preferences

<project-root>/
└── .xunxun/
    └── profile.md              # this project's learning context

current Session                # transient working state
```

Use non-empty `$XUNXUN_HOME` instead of `~/.xunxun` when explicitly configured.

Both profile files are private local state. Never commit, push, upload, or use them as telemetry. Reading an existing profile does not authorize unrelated writes.

If a location is unreadable or unwritable, continue with the remaining layers. Do not block teaching or claim that an update persisted.

## Discover the project profile

For a project-backed lesson:

1. use the Git worktree root when the material is inside one;
2. otherwise use the explicit workspace or project root supplied by the user;
3. read `<project-root>/.xunxun/profile.md` when it exists.

Do not search unrelated parent directories or a central project index. Locality is the identity: the profile next to the project belongs to that project.

## Opt in and protect project state

Do not create a project profile during an ordinary explanation. Obtain opt-in before first creation; an explicit request to save project learning progress is sufficient. Once the learner opts in and the file exists, compact milestone updates may continue during later lessons unless the learner withdraws that permission.

Before any project-profile write in a Git repository:

1. check whether `.xunxun/` is already tracked;
2. if tracked, do not write private state there; continue with Session state and explain the conflict when persistence matters;
3. if untracked, exclude `.xunxun/` through the repository's local `.git/info/exclude`, not its shared `.gitignore`;
4. verify the profile remains ignored before writing.

For a non-Git project, disclose that no version-control exclusion protects the file and ask before creation.

## What each layer owns

| Layer | Owns | Does not own |
|---|---|---|
| Global profile | stable and contextual teaching preferences across projects | project route, term lists, transcripts |
| Project profile | current route, established concepts, open gaps, project-scoped adaptations | unrelated projects, broad personality claims |
| Session | current question, draft explanation, new terminology bridges, weak hypotheses, immediate observations | durable history |

Do not persist terms individually. A project profile may summarize an established concept when that fact is needed to resume the route, but it is not a vocabulary list and has no introduced/working/demonstrated status.

## Read precedence

```text
current Session evidence
  > project .xunxun/profile.md
  > global .xunxun/profile.md
  > preset default
```

The narrower layer wins only where it contains relevant evidence. An unfamiliar overloaded term remains unfamiliar merely because a similarly named concept appeared in another project.

The learner's current explicit request overrides stored preferences. Replace or remove rejected preferences. When resuming a project lesson, check that the next referenced file and essential context still apply; a changed revision is a reason to inspect relevant changes, not to invalidate all progress.

## Persistence

At a natural milestone:

- keep short-lived observations in the Session;
- update an opted-in project profile when route, established understanding, open gaps, or a project-only adaptation must survive another Session;
- save a cross-project preference when explicitly asked, or confirm an inferred pattern before retaining it;
- replace or consolidate old conclusions instead of appending a chronological diary.

There is no automatic Session-end hook. Cross-Session continuity comes from loading a compact project profile, not replaying the prior conversation.

## Honest boundary

This is an instruction-driven Markdown convention, not a database. It has no locking, schema enforcement, account identity, telemetry, or cross-device synchronization. Add machinery only when concurrent writers or synchronization become real requirements.
