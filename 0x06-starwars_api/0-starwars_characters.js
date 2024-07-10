#!/usr/bin/node
const request = require('request');

function getMovieCharacters (movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(movieUrl, { json: true }, (err, res, body) => {
    if (err) {
      console.error(`Failed to fetch movie details: ${err.message}`);
      return;
    }

    const characterUrls = body.characters;
    characterUrls.forEach(url => {
      request(url, { json: true }, (err, res, body) => {
        if (err) {
          console.error(`Failed to fetch character details: ${err.message}`);
          return;
        }
        console.log(body.name);
      });
    });
  });
}

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: node star_wars_characters.js <movie_id>');
} else {
  getMovieCharacters(movieId);
}
