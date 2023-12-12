#!/usr/bin/node
let i = 2;
const { argv } = require('process');
if (argv[2] == null) {
  console.log('No argument');
} else {
  while (argv[i] != null) {
    console.log(argv[i]);
    i++;
  }
}
