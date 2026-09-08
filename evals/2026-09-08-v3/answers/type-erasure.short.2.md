Yes. TypeScript catches type mistakes **before the program runs**, but it doesn’t enforce those types while JavaScript is running.

Normally, this is rejected:

```ts
let age: number = "hello"; // TypeScript error
```

But unchecked external data or an escape hatch such as `any` can bypass that check:

```ts
let incoming: any = "hello"; // any disables type checking here
let age: number = incoming; // Accepted, but age holds a string
```

A **type assertion**—telling TypeScript to treat a value as a particular type—also doesn’t check or convert the value.

For external data, check it while the program runs:

```ts
if (typeof incoming === "number" && Number.isFinite(incoming)) {
  let age: number = incoming;
}
```

This accepts only actual finite numbers, excluding strings, `NaN`, and infinity.