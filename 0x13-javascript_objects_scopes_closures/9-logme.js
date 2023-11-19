#!/usr/bin/node
let iterator = 0;

exports.logMe = function (item) {
  console.log(iterator + ': ' + item);
  iterator++;
};
