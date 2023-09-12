#!/usr/bin/node
module.exports.nbOccurences = function (arr, num) {
  const temp = {};
  arr.forEach(
    (n) => {
      if (temp[n]) {
        temp[n]++;
      } else {
        temp[n] = 1;
      }
    }
  );
  return temp[num];
};
