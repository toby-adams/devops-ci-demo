import { sum } from "../src/sum";

test("adds two numbers", () => {
  expect(sum(2, 3)).toBe(5);
});

test("handles negative numbers", () => {
  expect(sum(-2, 3)).toBe(1);
});