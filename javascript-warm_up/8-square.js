#!/usr/bin/node

const x = parseInt(process.argv[2]);

if (isNaN(x)) {
  console.log('Missing size');
} else {
  for (let index = 0; index < x; index++) {
    console.log('X'.repeat(x));
  }
}
