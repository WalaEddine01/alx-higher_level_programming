$.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (params) {
  $('#character').text(params.name);
}).fail(function (xhr, status, error) {
  $('#character').text('Error fetching character data: ' + error);
});
