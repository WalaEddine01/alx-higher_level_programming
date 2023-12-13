#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i; let n = 0;
  for (i = 0; i < list.length; i++) {
    if (searchElement === list[i]) {
      n++;
    }
  }
  return n;
};
