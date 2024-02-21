#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const list = JSON.parse(body);
    const done = {};
    for (const todo of list) {
      if (todo.completed) {
        if (!done[todo.userId]) {
          done[todo.userId] = 1;
        } else {
          done[todo.userId]++;
        }
      }
    }
    console.log(done);
  }
});
