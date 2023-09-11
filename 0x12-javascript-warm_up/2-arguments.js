#!/usr/bin/node
const argv = process.argv;
const len = argv.length;
let message;
if (len > 2) {
  message = len === 3 ? 'Argument found' : 'Arguments found';
} else {
  message = 'No argument';
}
console.log(message);
