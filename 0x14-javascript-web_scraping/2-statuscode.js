#!/usr/bin/node
const { argv } = require('process');
const req = require('request');

req.get(argv[2], function (err, res, body) {
  if (err) {
    console.error('Error:', err);
  } else {
    console.log('code:', res.statusCode);
  }
});
