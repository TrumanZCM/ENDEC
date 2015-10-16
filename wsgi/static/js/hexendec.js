/**
 * Created by Truman on 10/14/15.
 */
$("#hexencoder").click(function () {
    var input = $("#hextext").val();
    var hex = '';
    for (var i = 0; i < input.length; i++) {
        hex += '' + input.charCodeAt(i).toString(16);
    }
    $('#hexresult').text(hex);
});

$("#hexdecoder").click(function () {
    var input = $("#hexext").val();
    var str = '';
    for (var i = 0; i < input.length; i += 2)
        str += String.fromCharCode(parseInt(input.substr(i, 2), 16))
    $('#hexresult').text(str);
});