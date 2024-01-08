#!/usr/bin/node
const { argv } = require('process');
if (argv.length <= 3) {
  console.log(0);
} else {
  const array = [];
  for (let i = 2; i < argv.length; i++) {
    !isNaN(parseFloat(argv[i])) && array.push(parseFloat(argv[i]));
  }
  array.sort(function (a, b) { return a - b; });
  console.log(array[array.length - 2]);
}
