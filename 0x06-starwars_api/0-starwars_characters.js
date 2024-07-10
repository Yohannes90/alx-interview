#!/usr/bin/node
const request = require('request');

function getMovieCharacters (movieId) {
  const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

  request(movieUrl, { json: true }, (err, res, body) => {
    if (err) {
      console.error(`Failed to fetch movie details: ${err.message}`);
      return;
    }

    if (res.statusCode !== 200) {
      console.error(`Failed to fetch movie details: ${res.statusCode} ${res.statusMessage}`);
      return;
    }

    const characterUrls = body.characters;
    let charactersFetched = 0;
    const characters = new Array(characterUrls.length);

    characterUrls.forEach((url, index) => {
      request(url, { json: true }, (err, res, body) => {
        if (err) {
          console.error(`Failed to fetch character details: ${err.message}`);
          return;
        }

        if (res.statusCode !== 200) {
          console.error(`Failed to fetch character details: ${res.statusCode} ${res.statusMessage}`);
          return;
        }

        characters[index] = body.name;
        charactersFetched++;

        // Only print characters when all have been fetched
        if (charactersFetched === characterUrls.length) {
          characters.forEach(character => console.log(character));
        }
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
