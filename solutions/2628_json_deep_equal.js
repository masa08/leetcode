function areDeeplyEqual(o1, o2) {
  // o1 and o2 are object and doesn't refer to same object.
  if (o1 === o2) return true;
  if (typeof o1 != 'object' || typeof o2 != 'object') return o1 === o2;

  // null
  if (o1 === null || o2 === null) return false;

  // array & object
  if (Object.prototype.toString.call(o1) !== Object.prototype.toString.call(o2))
    return false;

  // array comparison
  if (Array.isArray(o1)) {
    if (o1.length !== o2.length) return false;
    for (let i = 0; i < o1.length; i++) {
      console.log(o1[i], o2[i]);
      if (!areDeeplyEqual(o1[i], o2[i])) return false;
    }
    return true;
  }

  // object comparison
  if (Object.keys(o1).length !== Object.keys(o2).length) return false;
  for (const key in o1) {
    if (!areDeeplyEqual(o1[key], o2[key])) return false;
  }

  return true;
}
