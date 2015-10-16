/**
 * Created by Truman on 10/14/15.
 */
$('#urlencoder').click(function() {
    var input = $('#urltext').val();
    $('#urlresult').text(encodeURI(input));
});

$('#urldecoder').click(function() {
    var input = $('#urltext').val();
    $('#urlresult').text(decodeURI(input));
})