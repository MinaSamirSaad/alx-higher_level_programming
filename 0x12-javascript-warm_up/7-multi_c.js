#!/usr/bin/node
const { argv } = require('process');
const iterations = parseInt(argv[2]);
if (isNaN(iterations)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < iterations; i++) {
    console.log('C is fun');
  }
}
