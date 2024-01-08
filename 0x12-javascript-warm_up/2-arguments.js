#!/usr/bin/node
const { argv } = require('process');
if (argv.length > 2) {
  argv.length === 3 ? console.log('Argument found') : console.log('Arguments found');
} else {
  console.log('No argument');
}
