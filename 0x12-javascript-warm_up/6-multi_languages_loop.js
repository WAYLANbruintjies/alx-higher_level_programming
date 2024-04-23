#!/usr/bin/node
// A script that prints 3 lines using an array of string and a loop

const lines = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

while (lines) {
  console.log(`${lines[0]}\n${lines[1]}\n${lines[2]}`);
  break;
}
