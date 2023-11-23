#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async function (error, response, body) {
  if (!error) {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const name = await new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (!error) {
            resolve(JSON.parse(body).name);
          } else {
            reject(error);
          }
        });
      }
      );
      console.log(name);
    }
  }
}
);
