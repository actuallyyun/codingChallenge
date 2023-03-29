const containsDuplicate = (nums) => {
  let found = false;
  const sortedNums = nums.sort();
  for (let i = 0; i < sortedNums.length; i++) {
    if (sortedNums[i] === sortedNums[i + 1]) {
      found = true;
    }
  }
  return found;
};

export default containsDuplicate;
