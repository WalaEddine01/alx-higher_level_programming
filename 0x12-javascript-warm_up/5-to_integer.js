#!/usr/bin/node
const num = Number(process.argv[2]);
if (!isNaN(num)) {
  console.log(parseInt(num));
} else {
  console.log('Not a number');
}
