#!/usr/bin/node
// A script that prints a square

const sizeArg = process.argv[2];
const squareSize = parseInt(sizeArg);
const x = 'x';

if (isNaN(squareSize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < squareSize; i++) {
    console.log(x.repeat(squareSize));
  }
}
