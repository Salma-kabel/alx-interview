#!/usr/bin/node
const request = require('request');
const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movieId;
request(url, async function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      await printCharacters(characters, i);
    }
  }
});

function printCharacters (characters, i) {
  return new Promise((resolve, reject) => {
    const idlist = characters[i].split('/');
    const id = idlist[idlist.length - 2];
    request('https://swapi-api.alx-tools.com/api/people/' + id, function (err, response, body) {
      if (err) {
        console.log(err);
        reject(err);
      } else {
        console.log(JSON.parse(body).name);
        resolve();
      }
    });
  });
}
