#!/usr/bin/node
const argv = process.argv;
if (argv[2] == null) {
  console.log('No argument');
} else if (argv[3] == null) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
