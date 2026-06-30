#!/usr/bin/node
document.addEventListener('DOMContentLoaded', () => {
  const myRequests = new Request('https://hellosalut.stefanbohacek.com/?lang=fr');
  const thehello = document.getElementById('hello');

  fetch(myRequests)
    .then(response => response.json())
    .then(data => {
      thehello.textContent = data.hello;
    });
  });