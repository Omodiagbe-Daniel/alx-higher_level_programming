#!/usr/bin/node
function fact (num) {
  if (isNaN(num)) {
    return (1);
  } else if (num === 0) {
    return (1);
  }
  return (num * fact(num - 1));
}

const factorial = fact(parseInt(process.argv[2]));
console.log(factorial);
