#!/usr/bin/node
// writing data peovided by user to file provided by used

const fs = require('fs');

const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf-8', (err) => {
    if (err) {
        console.log(err);
    }
})
