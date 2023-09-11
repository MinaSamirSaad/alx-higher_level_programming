#!/usr/bin/node
const argv = require('process').argv;
const num = parseInt(argv[2], 10);
if (num) {
  for (let i = 0; i < num; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
