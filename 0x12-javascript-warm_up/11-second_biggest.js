#!/usr/bin/node
let num;
if (process.argv.length < 4) {
  num = 0;
} else {
  num = parseInt(process.argv.slice(2).sort((a, b)=>a - b).reverse()[1]);
}
console.log(num);
