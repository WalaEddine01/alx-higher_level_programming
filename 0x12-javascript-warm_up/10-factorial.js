#!/usr/bin/node
const argv = process.argv;
const n1 = parseInt(argv[2]);
function fact (n) {
  if (isNaN(n) || n == 1) {
    return 1;
  }
  return fact(n - 1) * n;
}
console.log(fact(n1));
