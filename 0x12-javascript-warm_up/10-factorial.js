#!/usr/bin/node
const argv = process.argv;
const num = parseInt(argv[2]);
console.log(factorial(num));
function factorial (num) {
  if (!num) {
    return (1);
  } else if (num === 0) {
    return (1);
  } else {
    return (num * factorial(num - 1));
  }
}
