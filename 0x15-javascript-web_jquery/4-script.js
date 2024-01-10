#!/usr/bin/node
const header = $('HEADER');

$('DIV#toggle_header').click(() => {
  header.toggleClass('red');
  header.toggleClass('green');
});
