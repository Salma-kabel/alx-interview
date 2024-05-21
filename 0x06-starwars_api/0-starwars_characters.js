#!/usr/bin/node
const request = require('request');
const movie_id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/' + movie_id
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else { 
    const characters = JSON.parse(body).characters;
    for (let i = 0; i < characters.length; i++) {
      print_characters(characters, i);
    }
  }
});

function print_characters (characters, i) {
  const idlist = characters[i].split('/');
  const id = idlist[idlist.length - 2];
  request('https://swapi-api.alx-tools.com/api/people/' + id, function (err, response, body) {
    if (err) {
      console.log(err);
    } else {
      console.log(JSON.parse(body).name);
    }
  });
}
