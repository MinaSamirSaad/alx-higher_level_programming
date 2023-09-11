#!/usr/bin/node
const argv = require('process').argv;
const num = parseInt(argv[2], 10);
if (num) {
  if (num > 0) {
    let mes = '';
    for (let j = 0; j < num; j++) {
      mes += 'x';
    }
    for (let i = 0; i < num; i++) {
      console.log(mes);
    }
  }
} else {
  console.log('Missing size');
}
