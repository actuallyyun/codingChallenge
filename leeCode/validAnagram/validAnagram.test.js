import { describe, expect, test } from "@jest/globals";
import validAnagram from "./validAnagram";

describe("test anagram", () => {
  test("s = 'anagram', t = 'nagaram'returns true", () => {
    const s = "anagram";
    const t = "nagaram";
    expect(validAnagram(s, t)).toBe(true);
  });
  test("'rat' and 'car' returns false", () => {
    const s = "rat";
    const t = "car";
    expect(validAnagram(s, t)).toBe(false);
  });
});
