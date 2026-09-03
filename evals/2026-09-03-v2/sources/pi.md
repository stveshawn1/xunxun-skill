# Pi source snapshot

Snapshot date: 2026-09-03.

From `packages/coding-agent/docs/session.md`:

```ts
interface SessionEntryBase {
  type: string
  id: string
  parentId: string | null
  timestamp: string
}
```

Sessions are JSONL files. The first line is a session header. Message and metadata entries are appended as separate lines. Version 2 introduced `id` and `parentId`, allowing branches to remain in one file. Loading a conversation follows the selected leaf's ancestry rather than treating every physical line as the active conversation.

Compaction is appended as another session entry. It stores a summary and identifies the recent portion to keep in the model context. Earlier events remain in the JSONL even though the model-facing context uses the summary plus retained messages.

From the agent-loop terminology:

- Turn: user input through the final assistant response with no more tool calls.
- Step: one model request and response, followed by any tool executions requested in that response.
- One Turn may contain several Steps. One Step may contain several parallel tool calls.

From `packages/coding-agent/docs/extensions.md` and usage docs:

- Extensions are executable TypeScript modules. They can subscribe to lifecycle events, register or intercept tools, add commands and UI, and append session entries. They run with host-process permissions.
- Skills are Markdown instructions made available to the model.
- Prompt templates expand user-selected prompt text.

Sources:

- <https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/session.md>
- <https://github.com/earendil-works/pi/blob/main/packages/coding-agent/docs/extensions.md>

