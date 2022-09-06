#!/usr/bin/node
const num = parseInt(process.argv[2]);
const str = 'C is fun';
let i = 0;
if (isNaN(num)) {
  console.log('Missing number of occurrences');
} else {
  while (i < num) {
    console.log(str);
    i++;
  }
}
