/*
  updating text color in header tag
*/
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function(data) {
  $('UL#list_movies').append(data.results[0].title);
});
