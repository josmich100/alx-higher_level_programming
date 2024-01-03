#!/usr/bin/node
const request = require("request");
const fs = require("fs");
const filePath = process.argv[3];
const url = "https://swapi-api.hbtn.io/api/films/" + process.argv[2];
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filePath, body, "utf-8", (err) => {
      if (err) {
        console.error(err);
      }
    });
  }
});
