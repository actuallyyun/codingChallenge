const twoSum = function (nums, target) {
  const numsMap = nums.map((num, index) => {
    return {
      number: num,
      index: index
    }
  })

  //sort map and exclude the bigger ones
  const filteredMap = numsMap.filter((e) => e.number <= target)
  console.log({ numsMap, filteredMap })

  for (let i = 0; i < filteredMap.length; i++) {
    const complement = target - filteredMap[i].number
    const complementIndex = filteredMap.findIndex(
      (n) => n.number === complement
    )
    if (complementIndex !== -1 && complementIndex !== i) {
      return [i, complementIndex]
      break
    }
  }
}

export default twoSum
