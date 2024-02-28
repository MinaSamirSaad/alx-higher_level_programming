const apiUrl = 'https://swapi-api.alx-tools.com/api/people/5/?format=json';
$.get(apiUrl, function (data, textStatus) {
  if (textStatus === 'success') {
    $('#character').text(data.name);
  }
});
