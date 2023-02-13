<!-- alert message timeout 5 sec. -->
setTimeout(function (){
    if ($('#msg').length>0){
    $('#msg').remove();
    }
}, 5000)
setTimeout(function (){
    if ($('.alert-danger').length>0){
    $('.alert-danger').remove();
    }
}, 5000)
setTimeout(function (){
    if ($('#error_1_id_password2').length>0){
    $('#error_1_id_password2').remove();
    }
}, 5000)

