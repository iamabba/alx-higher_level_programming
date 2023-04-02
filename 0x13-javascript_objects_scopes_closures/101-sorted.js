#!/usr/bin/node
const dict = require('./101-data').dict;

const result = {};

for (const key in dict) {
  const count = dict[key];
  if (count in result) {
    result[count].push(key);
  } else {
    result[count] = [key];
  }
}

console.log(result);
