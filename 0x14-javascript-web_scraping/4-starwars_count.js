#!/usr/bin/node
// This script prints the number of movies where the character “Wedge Antilles” is present

const request = require('request');

const apiUrl = process.argv[2];

request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.error(err);
  } else {
    const filmsData = JSON.parse(body);

    if (filmsData.results && filmsData.results.length > 0) {
      const moviesWithWedgeAntilles = filmsData.results.filter(movie =>
        movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
      );

      console.log(moviesWithWedgeAntilles.length);
    }
  }
});
