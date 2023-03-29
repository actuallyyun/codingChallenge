export function duplicateEncode1(word) {
  const arr = word.toLowerCase().split("");
  const newArr = arr.map((e) => {
    const eFound = arr.filter((_e) => _e === e);
    if (eFound.length > 1) {
      return ")";
    } else {
      return "(";
    }
  });
  return newArr.join("");
}

export function duplicateEncode2(word) {
  return word
    .toLowerCase()
    .split("")
    .map((element, i, arr) => {
      return arr.indexOf(element) === arr.lastIndexOf(element) ? "(" : ")";
    })
    .join("");
}

duplicateEncode2("din");

