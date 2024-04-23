#!/usr/bin/node
// A script that prints a message depending of the number of arguments passed

const args = process.argv.lenght;

if (args === 1) {
  console.log('No Argument');
} else if (args === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
