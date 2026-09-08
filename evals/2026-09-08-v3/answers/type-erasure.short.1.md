Yes. **TypeScript catches type mismatches before the program runs, but it doesn’t enforce types while it runs.**

Normally, it rejects this:

```ts
let age: number = "hello"; // TypeScript error
```

But you can bypass that check, for example with `any`, which disables type checking for a value:

```ts
let incoming: any = "hello";
let age: number = incoming; // Accepted, but age contains a string
```

Once the types are erased, JavaScript executes the program. The `number` annotation doesn’t convert the string or add a runtime check. A type assertion such as `incoming as number` doesn’t do either.

For external data, such as an API response, check the actual value:

```ts
if (typeof incoming === "number" && Number.isFinite(incoming)) {
  let age: number = incoming;
}
```

That accepts only finite numbers, rejecting strings, `NaN`, and infinity.