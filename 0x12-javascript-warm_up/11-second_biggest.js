#!/usr/bin/node
const argv = process.argv;
if (argv.length < 4) {
  console.log(0);
} else {
  let max1 = argv[2]; let max2 = argv[2]; let i = 3;
  while (i < argv.length) {
    if (parseInt(argv[i]) > parseInt(max1)) {
      max2 = max1;
      max1 = parseInt(argv[i]);
    }
    i++;
  }
  console.log(max2);
}
