#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const all = JSON.parse(body).characters;
    for (const cha of all) {
      request(cha, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});