const throttle = (fn, t) => {
  let lastArgs = null;
  let shouldCall = true;

  const execute = () => {
    if (shouldCall && lastArgs) {
      fn(...lastArgs); // 最初に実行

      lastArgs = null;
      shouldCall = false;

      setTimeout(() => {
        shouldCall = true;
        // tミリ秒後に、最新の引数で実行。引数がなければ実行しない。
        execute();
      }, t);
    }
  };

  return (...args) => {
    lastArgs = args; // 最新の引数を保存
    execute();
  };
};

/**
 * const throttled = throttle(console.log, 100);
 * throttled("log"); // logged immediately.
 * throttled("log"); // logged at t=100ms.
 */
