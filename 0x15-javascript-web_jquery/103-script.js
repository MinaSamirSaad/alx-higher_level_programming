// $(document).ready(function() === $(function ()
// it should wrap the code in a jQuery wrapper
$(function () {
  $('INPUT#btn_translate').click(function () {
    translate();
  });
  $('INPUT#language_code').keydown(function (event) {
    // Enter button keycode is 13
    if (event.keyCode === 13) {
      translate();
    }
  });
});

function translate() {
  const urlApi = 'https://hellosalut.stefanbohacek.dev/';
  const langApi = $('INPUT#language_code').val();
  $.get(urlApi, {lang: langApi}, function (data) {
    $('DIV#hello').text(data.hello);
  });
}
