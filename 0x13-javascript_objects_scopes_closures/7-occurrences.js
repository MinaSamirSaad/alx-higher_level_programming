#!/usr/bin/node
module.exports.nbOccurences = function (arr, num) {
  let counter = 0;
  for (let i = 0; i < arr.length; i++) {
    if (num === arr[i]) {
      counter++;
    }
  }

  return (counter);
};
