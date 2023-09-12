#!/usr/bin/node
const list = require('./100-data').list;
const newList = list.map((n, i) => n * i);
console.log(list);
console.log(newList);
