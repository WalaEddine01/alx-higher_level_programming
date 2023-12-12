#!/usr/bin/node
const { argv } = require('node:process');
if (argv[2] == null) {
  console.log('No argument');
} else if (argv[3] == null) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
