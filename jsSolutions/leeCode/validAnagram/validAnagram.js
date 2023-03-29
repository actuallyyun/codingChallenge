const validAnagram = (s, t) => {
  const sArray = [...s].sort();
  const tArray = [...t].sort();
  return (
    sArray.length === tArray.length &&
    sArray.every((s, index) => s === tArray[index])
  );
};

export default validAnagram;
