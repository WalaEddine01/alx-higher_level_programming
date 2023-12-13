#!/usr/bin/node
const Square2 = require('./5-square');

class Square extends Square2 {
  charPrint (c) {
    if (c !== undefined) {
      let i = 0; let j = 0;
      let X = '';
      for (i = 0; i < this.height; i++) {
        X = '';
        for (j = 0; j < this.width; j++) {
          X += c;
        }
        console.log(X);
      }
    } else {
      this.print();
    }
  }
}
module.exports = Square;
