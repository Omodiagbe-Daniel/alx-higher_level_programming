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
  let list = [];
  for (let z = 0; z < file.length; z++) {
    list.push(file[z].userId);
  }
  list = new Set(list);
  const obj = {};
  for (let i = 1; i <= list.size; i++) {
    let count = 0;
    for (let j = 0; j < file.length; j++) {
      if (file[j].userId === i && file[j].completed === true) {
        count++;
      }
    }
    if (count === 0) {
      return {}
    }
    obj[i] = count;
  }
  console.log(obj);
});
