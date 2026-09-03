# DeepSeek Harness source snapshot

Repository snapshot: `deepseek-ai/deepseek-harness@b150a551b8`.

From `packages/boot/app-boot/src/profile.ts` and `apps/cli/src/profile-boot.ts`:

- A Profile directory contains a `package.json` whose `dsh.profile.bundles` is an ordered package-name list, plus the Profile's own `cordis.patch.yml`.
- A Bundle is an npm package whose manifest points to its patch file.
- Composition starts from an empty entry list and applies bundle layers in order, then profile patch, home patch, command-line overlays, and launcher-derived overlays. Later layers have higher precedence.
- A Patch can insert plugin entries, target an entry by id to change config, or disable it.

From vendored Cordis:

```ts
export abstract class Service {
  constructor(protected ctx: Context, name: string) {
    // ...
    self.ctx.reflect.provide(name, self, this[symbols.check])
    return self
  }
}
```

`Context` returns a Proxy. Ordinary property reads use the service resolver. A Fiber represents one plugin application and owns dependency state, validated config, lifecycle effects, and cleanup. An `inject` declaration expresses required services; it does not convert a string into an object.

From core Session and headless runner:

- Session is an append-only sequence of events with continuous `seq` values.
- Model-facing messages are a projection folded from recorded surface events. Model-visible semantic content must have a recorded event; diagnostic events may be logged without becoming model-visible.
- Headless records its starting sequence, submits a user follow-up, waits for idle, flushes Session, scans that interval for `assistant/message` and `turn/end`, prints the last assistant text, and derives the exit code from the recorded end reason.

Source files:

- `packages/boot/app-boot/src/profile.ts`
- `apps/cli/src/profile-boot.ts`
- `vendor/cordis/src/context.ts`
- `vendor/cordis/src/service.ts`
- `vendor/cordis/src/fiber.ts`
- `packages/core/session/src/index.ts`
- `packages/core/session/src/surface.ts`
- `packages/bundle/headless/src/index.ts`

