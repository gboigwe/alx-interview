#!/usr/bin/node

// Import the request module for making HTTP requests
const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];

// Check if a movie ID was provided
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

// Base URL for the Star Wars API
const baseUrl = 'https://swapi-api.alx-tools.com/api';

// Make a request to get the film data
request(`${baseUrl}/films/${movieId}/`, (error, response, body) => {
  // Handle any errors that occurred during the request
  if (error) {
    console.error('Error:', error);
    return;
  }
  // Check if the response status code is OK (200)
  if (response.statusCode !== 200) {
    console.error('Invalid status code:', response.statusCode);
    return;
  }

  // Parse the JSON response
  const film = JSON.parse(body);
  // Get the list of character URLs
  const characters = film.characters;

  // Function to fetch a character's name from their URL
  const fetchCharacter = (url) => {
    return new Promise((resolve, reject) => {
      request(url, (error, response, body) => {
        if (error) reject(error);
        else if (response.statusCode !== 200) reject(new Error(`Invalid status code: ${response.statusCode}`));
        else resolve(JSON.parse(body).name);
      });
    });
  };

  // Use Promise.all to fetch all character names in parallel
  Promise.all(characters.map(fetchCharacter))
    // Print each character name on a new line
    .then(names => names.forEach(name => console.log(name)))
    .catch(error => console.error('Error:', error));
});
