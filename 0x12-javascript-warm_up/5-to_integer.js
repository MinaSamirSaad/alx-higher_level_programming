#!/usr/bin/node
const { argv } = require('process');
isNaN(parseFloat(argv[2])) ? console.log('Not a number') : console.log(`My number: ${parseFloat(argv[2])}`);
