#!/usr/bin/node
const args = process.argv;
if (args.length === 2 || args.length === 3) {
  console.log(0);
} else {
  const arr = args.slice(2, args.length - 1).sort();
  console.log(arr[arr.length - 2]);
}
