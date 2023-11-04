#!/usr/bin/node
/**
 * Construct another class that inherits from rectangle
 */
const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}

module.exports = Square;
