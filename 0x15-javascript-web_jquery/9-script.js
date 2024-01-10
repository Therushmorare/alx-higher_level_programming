$(document).ready(function(){
    $.ajax({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        success: function(data) {
            $("#hello").text(data.hello);
        },
        error: function(error) {
            console.log('Error fetching translation:', error);
        }
    });
});
