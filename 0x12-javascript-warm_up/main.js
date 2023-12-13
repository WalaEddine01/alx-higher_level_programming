#!/usr/bin/node
function Circle1 (radius) {
  return {
    radius,
    draw: function () {
      console.log('draw');
    }
  };
}
const Circle = Circle1(1);
Circle.draw();
console.log(Circle);
console.log(Circle.radius);
console.log('------------------');

function Circle2 (radius) {
  this.radius = radius;
  this.draw = function draw () {
    console.log('draw');
  };
}
const circle = new Circle2(1);
circle.draw();
console.log(circle);
console.log(circle.radius);
