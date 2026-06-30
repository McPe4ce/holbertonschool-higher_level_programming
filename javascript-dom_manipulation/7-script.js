#!/usr/bin/node

const theTitle = document.getElementById('list_movies');
const myRequest = new Request('https://swapi-api.hbtn.io/api/films/?format=json');
const listed = document.querySelector('ul')

fetch(myRequest).then(response => response.json().then(data => theTitle.textContent = data.title))
