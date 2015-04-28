$(document).ready(function(){
    $( "#tabs" ).tabs();

    $('.rating').rating({
        fx: 'float',
        image: 'http://127.0.0.1:8000/static/img/stars.png',
        loader: 'http://127.0.0.1:8000/static/img/ajax-loader.gif',
        minimal: 0.6,
        url: 'rating.php',
        callback: function(responce){

            this.vote_success.fadeOut(2000);
            if(responce.msg) alert(responce.msg);
        }
    });
    $.fn.editable.defaults.mode = 'inline';

    $('.editable').editable();
    $('.date').editable({
        format: 'yyyy-mm-dd',
        viewformat: 'dd/mm/yyyy',
        datepicker: {
                weekStart: 1
           }
        });
});
