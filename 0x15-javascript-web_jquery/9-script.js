const apiUrl = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
$.get(apiUrl, function (data, textStatus) {
  if (textStatus === 'success') {
    $('#hello').text(data.hello);
  }
});
