#!/usr/bin/node
const fs = require('fs');
const { argv } = require('process');

const fileName = argv[2];
const fileContent = argv[3];

fs.writeFileSync(fileName, fileContent, 'utf-8', (err) => {
  if (err) throw err;
}
);
