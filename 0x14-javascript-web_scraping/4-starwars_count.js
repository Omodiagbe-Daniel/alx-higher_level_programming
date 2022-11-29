#!/usr/bin/node
/*
  a script that prints the number of movies
  where the character “Wedge Antilles” is present
*/

const request = require('request');
let file = [];
const url = process.argv[2];
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  file = JSON.parse(body).results;
  let count = 0;
  for (let i = 0; i < file.length; i++) {
    for (const key in file[i]) {
      if (key === 'characters') {
        for (const k in file[i][key]) {
          if (file[i][key][k].endsWith('18/')) {
            count++;
          }
        }
      }
    }
  }
  console.log(count);
});
