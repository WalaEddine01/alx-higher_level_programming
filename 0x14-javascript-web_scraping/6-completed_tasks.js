#!/usr/bin/node
const { argv } = require('process');
const req = require('request');
const url = argv[2];
const data = {};
req.get(url, function (err, resp, body) {
  if (err) throw err;
  const cont = JSON.parse(body);
  cont.forEach(element => {
    if (element.completed === true) {
      if (!data[element.userId]) {
        data[element.userId] = 1;
      } else {
        data[element.userId] += 1;
      }
    }
  });
  console.log(data);
});
