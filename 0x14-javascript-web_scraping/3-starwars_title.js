#!/usr/bin/node
// display the status code of a GET request

const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${id}`;

request.get(url, (err, response, body) => {
    if (err) {
        console.log(err);
    } else {
        const data = JSON.parse(body);
        if (data.title) {
            console.log(data.title);
        } else {
            console.log('Not found');
        }
    }
});
