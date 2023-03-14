#!/usr/bin/node

const { list } = require('./100-data');
const factorIndex = (value, index) => value * index;
const newList = list.map(factorIndex);
console.log(list);
console.log(newList);
