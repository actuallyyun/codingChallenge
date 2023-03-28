const twoSum = function (nums, target) {
  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i]
    const complementIndex = nums.findIndex((n) => n === complement)
    if (complementIndex !== -1 && complementIndex !== i) {
      return [i, complementIndex]
      break
    }
  }
}

export default twoSum
