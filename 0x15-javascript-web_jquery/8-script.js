const apiUrl = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.get(apiUrl, function (data, textStatus) {
  if (textStatus === 'success') {
    for (const film of data.results) {
      $('#list_movies').append(`<li>${film.title}</li>`);
    }
  }
});
