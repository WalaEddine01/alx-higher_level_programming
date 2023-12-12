#!/usr/bin/node
let i = 2;
const args = process.argv;
if (args[2] == undefined) {
  console.log('No argument');
} else {
  while (args[i] != undefined) {
    console.log(args[i]);
    i++;
  }
}
