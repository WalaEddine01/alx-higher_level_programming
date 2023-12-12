#!/usr/bin/node
const argv = process.argv;
if (isNaN(Number(argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  let i = 0;
  while (i < Number(argv[2])) {
    console.log('C is fun');
    i++;
  }
}
