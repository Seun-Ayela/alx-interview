// #!/usr/bin/node
// /**
//  * Prints all characters of a Star Wars movie
//  * The first positional argument passed is the Movie ID
//  * Display one character name per line in the same order
//  * as  list in the /films/ endpoint
//  */

// const request = require('request');
// const filmNum = process.argv[2] + '/';
// const filmURL = 'https://swapi-api.hbtn.io/api/films/';
// // Makes API request, sets async to allow await promise
// request(filmURL + filmNum, async (err, res, body) => {
//   if (err) return console.error(err);

//   // find URLs of each character in the film as a list obj
//   const charURLList = JSON.parse(body).characters;

//   // Use URL list to character pages to make new requests
//   // await queues requests until they resolve in order
//   for (const charURL of charURLList) {
//     await new Promise((resolve, reject) => {
//       request(charURL, (err, res, body) => {
//         if (err) return console.error(err);

//         // finds each character name and prints in URL order
//         console.log(JSON.parse(body).name);
//         resolve();
//       });
//     });
//   }
// });


// #!/usr/bin/node
// * Prints all characters of a Star Wars movie
//  * The first positional argument passed is the Movie ID
//  * Display one character name per line in the same order
//  * as  list in the /films/ endpoint
//  */

#!/usr/bin/node


const request = require('request');

if (process.argv.length > 2) {
  request(`https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`, (err, res, body) => {
    if (err) console.log(err);
    const json = JSON.parse(body);
    const characters = json.characters.map(
      (item) => new Promise((resolve, reject) => {
        request(item, (err, res, body) => {
          if (err) reject(err);
          resolve(JSON.parse(body).name);
        });
      }));

    Promise.all(characters)
      .then((names) => console.log(names.join('\n')))
      .catch((err) => console.log(err));
  });
}