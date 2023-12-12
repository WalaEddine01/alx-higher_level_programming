#!/usr/bin/node
const argv = process.argv;
if (isNaN(Number(argv[2]))) {
  console.log('Missing size');
} else {
  let i = 0;
  let x = '';
  while (i < Number(argv[2])) {
    let j = 0;
    while (j < Number(argv[2])) {
      x += 'X';
      j++;
    }
    console.log(x);
    x = '';
    i++;
  }
}
