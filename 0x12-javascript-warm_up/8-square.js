#!/usr/bin/node
const num = parseInt(process.argv[2]);
const str = 'X';
if (isNaN(num)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++) {
    console.log(str.repeat(num));
  }
}
