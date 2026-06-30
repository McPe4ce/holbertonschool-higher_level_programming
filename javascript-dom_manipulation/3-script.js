#!/usr/bin/node

document.querySelector('#toggle_header').addEventListener('click', () => {
    if (document.querySelector('header').classList.contains('red')) {
        document.querySelector('header').classList.replace('red', 'green');
    } else {
        document.querySelector('header').classList.replace('green','red');
    }
})