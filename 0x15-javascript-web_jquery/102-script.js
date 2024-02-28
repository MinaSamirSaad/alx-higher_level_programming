// $(document).ready(function() === $(function ()
// it should wrap the code in a jQuery wrapper
$(function () {
  const urlApi = 'https://hellosalut.stefanbohacek.dev/';
  $('INPUT#btn_translate').click(function () {
    const langApi = $('INPUT#language_code').val();
    $.get(urlApi, {lang: langApi}, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
