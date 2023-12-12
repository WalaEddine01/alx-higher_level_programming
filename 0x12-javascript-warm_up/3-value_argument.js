#!/usr/bin/node
let i = 2;
const { argv } = require('process');
if (argv[2] == undefined) {
  console.log('No argument');
} else {
  while (argv[i] != undefined) {
    console.log(argv[i]);
    i++;
  }
}
