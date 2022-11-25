#!/usr/bin/node

const dict = require('./101-data').dict;
const arr = [];
const obj = {};
for (const key in dict) {
  arr.push(dict[key]);
}
const arr1 = new Set(arr);
for (const ele of arr1.values()) {
  const arr2 = [];
  for (const val in dict) {
    if (ele === dict[val]) {
      arr2.push(val);
    }
    obj[ele] = arr2;
  }
}
console.log(obj);
