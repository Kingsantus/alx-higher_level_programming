#!/usr/bin/node
// printing all character peculiar to a particular id

const request = require('request');

const id = process.argv[2];

const url = `https://swapi-api.hbtn.io/api/films/${id}`;

request(url, (error, resp, body) => {
  if (error) { console.log(err); }
  const data = JSON.parse(body);
  for (const charURL of data.characters) {
    request(charURL, (err, r, body) => {
      if (err) { console.log(err); }
      const data = JSON.parse(body);
      console.log(data.name);
    });
  }
});
