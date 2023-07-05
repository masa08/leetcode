/**
 * @param {Function} fn
 * @return {Array}
 */
Array.prototype.groupBy = function (fn) {
  const result = {};
  for (const el of this) {
    const key = fn(el);
    if (key in result) {
      result[key].push(el);
    } else {
      result[key] = [el];
    }
  }

  return result;
};

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */
