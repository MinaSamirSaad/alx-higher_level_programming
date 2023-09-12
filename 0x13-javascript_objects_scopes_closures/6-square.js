#!/usr/bin/node
const Sq = require('./5-square');
module.exports = class Square extends Sq {
  charPrint (c = 'x') {
    for (let i = 0; i < this.width; i++) {
      console.log(c.repeat(this.height));
    }
  }
};
