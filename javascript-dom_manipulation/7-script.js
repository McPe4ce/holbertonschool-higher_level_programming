#!/usr/bin/node

const theTitle = document.getElementById('list_movies');
const myRequest = new Request('https://swapi-api.hbtn.io/api/films/?format=json');


fetch(myRequest)
  .then(response => response.json())
  .then(data => data.results.forEach(film => {
    const listed = document.createElement('li');
    listed.textContent = film.title;
    theTitle.appendChild(listed);
  }));

