#!/usr/bin/node
const argv = require('process').argv;
const len = argv.length;
if (len > 2) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
