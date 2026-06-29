#!/usr/bin/node

const x = process.argv[2];
if (x === undefined || !Number.isInteger(parseInt(x))) {
  console.log('Missing number of occurrences');
}

let index;

for (index = 0; index < x; index++) {
  console.log('C is fun');
}
