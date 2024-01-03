#!/usr/bin/node
const request = require('request');
const episode = process.argv[2];
const apiUrl = `http://swapi.co/api/films/${episode}`;
request.get(apiUrl, (error, response, body) => {
  if (error) console.log(error);
  console.log(JSON.parse(body).title);
});
