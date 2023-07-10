/**
 * @param {any[]} arr
 * @param {number} depth
 * @return {any[]}
 */
var flat = function (arr, n) {
  if (n == 0) return arr;
  const result = [];

  const flatten = (nums, l) => {
    for (const num of nums) {
      if (Array.isArray(num) && l > 0) {
        flatten(num, l - 1);
      } else {
        result.push(num);
      }
    }
  };

  flatten(arr, n);

  return result;
};
