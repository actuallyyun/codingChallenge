import { describe, expect, test } from '@jest/globals'
import twoSum from './twoSum'

describe('test twoSum', () => {
  test("nums = [3,2,4], target = '6", () => {
    const nums = [3, 2, 4]
    const target = 6
    expect(twoSum(nums, target)).toEqual([1, 2])
  })
  test('[3,3] and 6 returns [0,1]', () => {
    const nums = [3, 3]
    const t = 6
    expect(twoSum(nums, t)).toEqual([1, 0])
  })
  test('[2,7,11,15] and 9 returns [0,1]', () => {
    const nums = [2, 7, 11, 15]
    const t = 9
    expect(twoSum(nums, t)).toEqual([0, 1])
  })
})
