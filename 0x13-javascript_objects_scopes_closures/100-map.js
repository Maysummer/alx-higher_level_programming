#!/usr/bin/node
const list = require('./100-data').list;
const newArr = list.map(i => i * list.indexOf(i));
console.log(list);
console.log(newArr);
