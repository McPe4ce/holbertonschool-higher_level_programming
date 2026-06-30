#!/usr/bin/node

const myRequest = new Request('https://swapi-api.hbtn.io/api/people/5/?format=json');
const myName = document.querySelector('#character');

fetch(myRequest).then(response => response.json()).then(data => { myName.textContent = data.name; });
