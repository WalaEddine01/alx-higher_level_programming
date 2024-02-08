$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function (params) {
  let newItem;
  for (let i = 0; i < params.results.length; i++) {
    newItem = $('<li>').text(params.results[i].title);
    $('#list_movies').append(newItem);
  }
});
