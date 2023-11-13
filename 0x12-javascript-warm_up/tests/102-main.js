#!/usr/bin/node

const addMeMaybe = require('../102-add_me_maybe');

function myFunction (number) {
  console.log('The number is:', number);
}

addMeMaybe(6, myFunction);
