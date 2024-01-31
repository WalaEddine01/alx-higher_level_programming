#!/usr/bin/node
const { argv } = require('process');
const req = require('request');
const fs = require('fs');

const url = argv[2];
const file = argv[3];
req.get(url, function (err, resp, body) {
  if (err) throw err;
  fs.writeFile(file, body, 'utf-8', (err) => {
    if (err) {
      console.log(err);
    }
  });
});
