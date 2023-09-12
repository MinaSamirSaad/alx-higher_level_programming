#!/usr/bin/node
exports.converter = (base) => (num) => {
  return (num.toString(base));
};
