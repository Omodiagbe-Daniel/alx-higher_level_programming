#!/usr/bin/node
exports.addMeMaybe = function addMeMaybe (num, func) {
  num = num + 1;
  func(num);
};
