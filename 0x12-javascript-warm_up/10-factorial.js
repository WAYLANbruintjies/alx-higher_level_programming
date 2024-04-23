#!/usr/bin/node
// Computes and prints a factorial

function factorial(n) {
  if (isNaN(n)) {
    return 1;
  } else if (n === 0) {
    return 1;
  } else {
    n * factorial(n - 1);
  }
}

const num = parseInt(process.argv[2]);
let res = factorial(num);

console.log(res);
