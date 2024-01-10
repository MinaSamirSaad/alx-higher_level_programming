#!/usr/bin/node
exports.esrever = function (list) {
  const revArr = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revArr.push(list[i]);
  }
  return revArr;
};
