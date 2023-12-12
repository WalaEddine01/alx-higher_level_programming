#!/usr/bin/node
const length_ = process.argv.length;
if (length_ < 3) {
  console.log('No argument');
} else if (length_ < 4) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
