#!/usr/bin/node
// This script reads and prints the content of a file

const fs = require('fs');
const filepath = process.argv[2];

fs.readFile(filepath, 'UTF-8', (err, content) => {
  if (err) {
	  console.log(err);
	}
else {
  	console.log(content);
}
});
