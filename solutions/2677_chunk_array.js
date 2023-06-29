/**
 * @param {Array} arr
 * @param {number} size
 * @return {Array[]}
 */
var chunk = function (arr, size) {
  let chunkedArray = [];
  let index = 0;
  while (index < arr.length) {
    chunkedArray.push(arr.slice(index, index + size));
    index += size;
  }
  return chunkedArray;

  // result = []
  // let left = arr.length
  // let current = 0
  // let copy = [...arr]

  // while (left > 0) {
  //   console.log(current, size)
  //   const target = copy.splice(current, size)
  //   result.push(target)
  //   left -= size
  //   current += size
  //   copy = [...arr]
  // }

  // return result
};
