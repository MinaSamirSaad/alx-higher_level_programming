#!/usr/bin/node
const dict = require('./101-data').dict;
const newDict = {};
Object.keys(dict).forEach((v) => {
  if (!newDict[dict[v]]) {
    newDict[dict[v]] = [];
  }
  newDict[dict[v]].push(v);
});
console.log(newDict);
