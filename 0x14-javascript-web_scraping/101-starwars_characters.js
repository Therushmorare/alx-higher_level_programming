#!/usr/bin/node
//starwars characters
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: node 101-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
  } else if (response.statusCode !== 200) {
    console.error('Failed to retrieve data. Status code:', response.statusCode);
  } else {
    const movieData = JSON.parse(body);
    const charactersUrls = movieData.characters;

    const fetchCharacterData = (url) => {
      return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
          if (error) {
            reject(error);
          } else if (response.statusCode !== 200) {
            reject(`Failed to retrieve character data. Status code: ${response.statusCode}`);
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    };

    Promise.all(charactersUrls.map(fetchCharacterData))
      .then((characterNames) => {
        characterNames.forEach((name) => {
          console.log(name);
        });
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }
});

