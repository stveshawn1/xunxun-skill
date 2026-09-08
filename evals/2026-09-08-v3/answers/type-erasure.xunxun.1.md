Yes. **TypeScript checks types before the program runs; it doesn’t enforce them while it runs.** After the types are removed, JavaScript executes the program.

TypeScript normally catches a direct mismatch:

```ts
let count: number = "hello"; // TypeScript reports an error
```

But you can bypass that check. A *type assertion* tells TypeScript to trust you:

```ts
let value: any = "hello"; // `any` disables type checking here
let count: number = value as number;
```

While running, `count` still contains `"hello"`. **`as number` neither converts the string nor checks that it is a number.**

For data coming from outside your program, you need a check that actually runs:

```ts
if (typeof value === "number" && Number.isFinite(value)) {
  // value is a finite number here
}
```

Think of `: number` as a rule TypeScript checks in your code, rather than a lock on what the variable can hold during execution.