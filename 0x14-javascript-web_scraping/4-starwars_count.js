#!/usr/bin/node

const request = require('request');

request.get(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    let counter = 0;
    const films = JSON.parse(body).results;
    for (const movies of films) {
      for (const ch of movies.characters) {
        if (ch.endsWith('18/')) {
          counter++;
        }
      }
    }
    console.log(counter);
  }
});
