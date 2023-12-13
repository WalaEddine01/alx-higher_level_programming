#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      return;
    }
    this.width = w;
    this.height = h;
  }

  print () {
    let i = 0; let j = 0;
    let X = '';
    for (i = 0; i < this.height; i++) {
      X = '';
      for (j = 0; j < this.width; j++) {
        X += 'X';
      }
      console.log(X);
    }
  }

  rotate () {
    const a = this.height;
    this.height = this.width;
    this.width = a;
  }

  double () {
    this.width = this.width * 2;
    this.height = this.height * 2;
  }
}
module.exports = Rectangle;
