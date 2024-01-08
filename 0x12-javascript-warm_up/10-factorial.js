#!/usr/bin/node
const { argv } = require('process');
function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  }
  return (n * factorial(n - 1));
}
console.log(factorial(parseInt(argv[2])));
