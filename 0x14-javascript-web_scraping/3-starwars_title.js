#!/usr/bin/node
const { argv } = require('process');
const req = require('request');

const url = 'https://swapi-api.alx-tools.com/api/films/' + argv[2];
req.get(url, function (err, res, body) {
  if (err) {
    console.error('Error:', err);
  } else {
    const cont = JSON.parse(body);
    console.log(cont.title);
  }
}
);
