#!/usr/bin/node
// A script that prints the first argument passed to it
const [arg] = process.argv.slice(2);

if (!arg) {
  console.log("No argument");
} else {
  console.log(arg);
}
