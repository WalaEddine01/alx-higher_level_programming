#!/usr/bin/node
const { argv } = require('process');
const req = require('request');
let i = 0;
req.get(argv[2], function (err, rep, body) {
  if (err) throw err;
  const cont = JSON.parse(body);
  cont.results.forEach(item => {
    item.characters.forEach(character => {
      if (character.includes(18)) {
        i += 1;
      }
    });
  });
  console.log(i);
}
);
