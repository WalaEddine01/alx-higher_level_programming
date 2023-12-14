#!/usr/bin/node
const argv = process.argv;
if (!isNaN(Number(argv[2]))) {
  console.log('My number: ' + parseInt(Number(argv[2])));
} else {
  console.log('Not a number');
}
