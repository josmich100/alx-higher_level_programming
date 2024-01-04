#!/usr/bin/node
//Write a script that computes the number of tasks completed by user id.
//The first argument is the API URL: https://jsonplaceholder.typicode.com/todos
//You must use the module request
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const task of tasks) {
      if (task.completed) {
        if (completed[task.userId]) {
          completed[task.userId]++;
        } else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
});
