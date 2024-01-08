#!/usr/bin/node
const { argv } = require('process');
const size = parseInt(argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
