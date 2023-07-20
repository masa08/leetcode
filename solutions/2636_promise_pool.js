/**
 * @param {Function[]} functions
 * @param {number} n
 * @return {Promise<any>}
 */
const promisePool = async (functions, n) => {
  return new Promise((resolve, _) => {
    let inProgressCount = 0;
    let functionIndex = 0;

    const helper = () => {
      if (functionIndex >= functions.length) {
        if (inProgressCount === 0) resolve();
        return;
      }

      while (inProgressCount < n && functionIndex < functions.length) {
        inProgressCount++;
        const promise = functions[functionIndex]();
        functionIndex++;
        promise.then(() => {
          inProgressCount--;
          helper();
        });
      }
    };
    helper();
  });
};

/**
 * const sleep = (t) => new Promise(res => setTimeout(res, t));
 * promisePool([() => sleep(500), () => sleep(400)], 1)
 *   .then(console.log) // After 900ms
 */
