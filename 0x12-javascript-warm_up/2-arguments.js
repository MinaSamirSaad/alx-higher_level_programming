#!/usr/bin/node
const { argv } = require('process');
argv.length > 2 ? console.log('Arguments found') : console.log('No argument');
