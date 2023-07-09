/**
 * @param {Array} arr1
 * @param {Array} arr2
 * @return {Array}
 */
var join = function (arr1, arr2) {
  const map = new Map();
  for (const obj of arr1) map.set(obj.id, obj);
  for (const obj of arr2) {
    if (map.has(obj.id)) {
      const prev = map.get(obj.id);
      for (const key of Object.keys(obj)) prev[key] = obj[key];
    } else {
      map.set(obj.id, obj);
    }
  }

  const result = [];
  for (const key of map.keys()) result.push(map.get(key));
  return result.sort((a, b) => a.id - b.id);
};
