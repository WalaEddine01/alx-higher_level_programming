#!/usr/bin/node
const { argv } = require('node:process');
const length = argv.length;
if (length < 3) {
  console.log('No argument');
} else if (length < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
