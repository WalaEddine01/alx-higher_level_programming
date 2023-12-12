#!/usr/bin/node
const args = process.argv;
if (args[2] == null) {
  console.log('No argument');
} else {
  let i = 2;
  while (args[i] != null) {
    console.log(args[i]);
    i++;
  }
}
