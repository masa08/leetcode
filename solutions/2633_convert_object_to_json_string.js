/**
 * @param {any} object
 * @return {string}
 */
var jsonStringify = function (object) {
  // null
  if (object === null) {
    return 'null';
  }

  // array
  if (Array.isArray(object)) {
    const elements = object.map((e) => jsonStringify(e));
    return `[${elements.join(',')}]`;
  }

  // object
  if (typeof object === 'object') {
    const keys = Object.keys(object);
    const kvPairs = keys.map((k) => `"${k}":${jsonStringify(object[k])}`);
    return `{${kvPairs.join(',')}}`;
  }

  // string
  if (typeof object === 'string') {
    return `"${object}"`;
  }

  return String(object);
};
