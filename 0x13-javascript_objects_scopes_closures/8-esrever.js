#!/usr/bin/node
exports.esrever = function (list) {
  if (list.length === 0) { return; }
  let i; let n = list.length; let tmp;
  for (i = 0; i <= n / 2; i++) {
    tmp = list[n - 1];
    list[n - 1] = list[i];
    list[i] = tmp;
    n--;
  }
  return list;
};
