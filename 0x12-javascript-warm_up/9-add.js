#!/usr/bin/node
const { argv } = require('process');
function add (a, b) {
  return (a + b);
}
console.log(add(parseFloat(argv[2]), parseFloat(argv[3])));
