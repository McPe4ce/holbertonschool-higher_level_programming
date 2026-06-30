#!/usr/bin/node

document.querySelector('#update_header').addEventListener('click', () => {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});
