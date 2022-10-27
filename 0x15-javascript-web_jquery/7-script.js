/*
  fetching data from a url
*/

$.get('https://swapi-api.hbtn.io/api/people/5/?format=json', function(data) {
  $("#character").html(data.name);
});
