#!/usr/bin/node

/*
  a script that prints all characters of a Star Wars movie
*/

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request.get(url + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const file = JSON.parse(body).characters;
  for (let i = 0; i < file.length; i++) {
    request.get(file[i], function (err, response, body) {
      if (err) {
        console.log(err);
      }
      const file2 = JSON.parse(body);
      console.log(file2.name);
    });
  }
});
