/**
 * @param {Object} obj
 * @return {Object}
 */
const compactObject = function (obj) {
  const dfs = (obj) => {
    // base case
    if (!Boolean(obj)) return false;
    if (typeof obj !== 'object') return obj;

    // for array
    if (Array.isArray(obj)) {
      const newArr = [];
      for (let i = 0; i < obj.length; i++) {
        const curr = obj[i];
        const res = dfs(curr);

        if (res) newArr.push(res);
      }
      return newArr;
    }

    // for object
    const newObj = {};
    for (const key in obj) {
      const res = dfs(obj[key]);
      if (res) {
        newObj[key] = res;
      }
    }
    return newObj;
  };

  return dfs(obj);
};
