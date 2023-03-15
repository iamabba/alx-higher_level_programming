#!/usr/bin/node
const dict = require('./101-data').dict;

let result = {};

for (let key in dict) {
  let count = dict[key];
  if (count in result) {
    result[count].push(key);
  } else {
    result[count] = [key];
  }
}

console.log(result);
