/**
 * @param {Array<Function>} functions
 * @return {Promise<any>}
 */
var promiseAll = async function (functions) {
  return new Promise((resolve, reject) => {
    const results = new Array(functions.length).fill(null);
    let unresolved = functions.length;

    functions.forEach(async (f, idx) => {
      try {
        const value = await f();
        results[idx] = value;
        unresolved -= 1;
        if (unresolved == 0) resolve(results);
      } catch (err) {
        reject(err);
      }
    });
  });
};

/**
 * const promise = promiseAll([() => new Promise(res => res(42))])
 * promise.then(console.log); // [42]
 */
