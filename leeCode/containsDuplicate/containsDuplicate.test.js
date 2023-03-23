import { describe, expect, test } from "@jest/globals";
import containsDuplicate from "./containsDuplicate";

describe("contains duplicate func", () => {
  test("array [1, 2, 3, 1] reurns true", () => {
    expect(containsDuplicate([1, 2, 3, 1])).toBe(true);
  });
  test("array [1,2,3,4] returns false", () => {
    expect(containsDuplicate([1, 2, 3, 4])).toBe(false);
  });
  test("array [1,1,1,3,3,4,3,2,4,2] returns true", () => {
    expect(containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])).toBe(true);
  });
});
