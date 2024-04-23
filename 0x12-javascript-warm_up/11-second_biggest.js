#!/usr/bin/node
// Searches the second biggest integer in the list of arguments

const list = process.argv.slice(2);
const nums = list.map(arg => parseInt(arg));

if (nums.length < 2) {
  console.log(0);
} else {
  let sortedNums = nums.sort((a, b) => b - a);
  console.log(sortedNums[1]);
}
