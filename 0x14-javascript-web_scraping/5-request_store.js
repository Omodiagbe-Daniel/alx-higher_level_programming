#!/usr/bin/node

/*
  a script that gets the contents of a webpage and stores it in a file
*/

const fs = require('fs');
const request = require('request');
const url = process.argv[2];
request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const file = (body);
  fs.writeFile(process.argv[3], file, (err) => {
    if (err) throw err;
  });
});
