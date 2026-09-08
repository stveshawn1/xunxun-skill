Yes. **TypeScript checks types before the program runs, but it doesn’t enforce them while it runs.** JavaScript executes the program after the type annotations are removed.

TypeScript catches a straightforward mistake:

```ts
let age: number = "hello"; // TypeScript reports an error
```

But you can bypass that check with `any`:

```ts
let value: any = "hello";
let age: number = value; // No type error, but age contains a string
```

A type assertion such as `value as number` also doesn’t convert or validate the value—it just tells TypeScript to trust you.

For data coming from outside your program, check it at runtime:

```ts
if (typeof value === "number" && Number.isFinite(value)) {
  // value is a finite number here
}
```

Think of the `number` annotation as a rule the checker uses, rather than a lock on what the variable can hold.