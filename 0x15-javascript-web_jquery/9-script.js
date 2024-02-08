$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function (params) {
  $('#hello').text(params.hello);
});
