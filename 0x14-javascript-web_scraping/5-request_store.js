#!/usr/bin/node
// getting the contents of a webpage and stores it in a file

const fs = require('fs');
const request = require('request');

const url = process.argv[2];
const filePath = process.argv[3];

request.get(url, (err, response, body) => {
    if (err) {
        console.log(err);
    } else {
        fs.writeFile(filePath, body, 'utf-8', (writeerr) => {
            if (writeerr) {
                console.log(writeerr);
            }
        });
    }
});
