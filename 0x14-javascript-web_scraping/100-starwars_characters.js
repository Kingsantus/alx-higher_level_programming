#!/usr/bin/node
// printing all character peculiar to a particular id

const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, (error, response, body) => {
  if (error) { console.log(error); }
  const result = JSON.parse(body);
  for (const charURL of result.characters) {
    request(charURL, (err, r, body) => {
      if (err) { console.log(err); }
      const result = JSON.parse(body);
      console.log(result.name);
    });
  }
});
