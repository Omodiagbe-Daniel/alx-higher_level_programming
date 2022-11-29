#!/usr/bin/node

/*
  a script that computes the number of tasks completed by user id
*/

const request = require('request');
const url = process.argv[2];

request.get(url, function (err, response, body) {
  if (err) {
    console.log(err);
  }
  const file = JSON.parse(body);
  const obj = {};
  for (let i = 1; i <= 10; i++) {
    let count = 0;
    for (let j = 0; j < 200; j++) {
      if (file[j].userId === i && file[j].completed === true) {
        count++;
      }
    }
    obj[i] = count;
  }
  console.log(obj);
});
