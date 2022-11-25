#!/usr/bin/node

const list = require('./100-data.js').list;

const map2 = list;
const map1 = map2.map((x, index) => {
  return x * index;
});
console.log(map2);
console.log(map1);
