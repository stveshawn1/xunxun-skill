Yes. **TypeScript can catch the mistake before your code runs, but it doesn’t enforce types while it runs.**

For example, TypeScript normally flags this:

```ts
let age: number = "hello"; // Type error
```

But you can bypass that check with `any`:

```ts
let value: any = "hello";
let age: number = value; // Passes the type check
```

When this runs, `age` contains `"hello"`. The `number` annotation has been removed; it doesn’t convert the string or protect the variable.

This matters when receiving external data, such as an API response. Even writing `value as number` only tells TypeScript to trust you—it doesn’t check or convert anything. To ensure the value really is a finite number, check it while the program runs:

```ts
if (typeof value === "number" && Number.isFinite(value)) {
  // Here, value really is a finite number.
}
```