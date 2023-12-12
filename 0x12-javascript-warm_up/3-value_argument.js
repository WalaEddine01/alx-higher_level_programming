#!/usr/bin/node
const { argv } = require('process');
if (argv[2] == null) {
  console.log('No argument');
} else {
  let i = 2;
  while (argv[i] != null) {
    console.log(argv[i]);
    i++;
  }
}
