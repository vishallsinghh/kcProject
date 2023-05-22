

$(document).ready(function() {

    var base_url = window.location.origin;
    
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }   
$('#buyformid').on('submit', function(e) {
        e.preventDefault(); // avoid to execute the actual submit of the form.
        
        var form = $(this);
        var url = base_url+"/buy/";
        var fd = new FormData();    
        var csrftoken = getCookie('csrftoken');
        fd.append('email',$("#email").val())
        fd.append('name',$("#name").val())
        fd.append('odoo_version',$("#odoo_version").val())
        fd.append('odoo_product',$("#odoo_product").val())
        console.log("csrf :",csrftoken);
        $.ajax({
               type: "POST",
               url: url,
               data: fd, 
               headers: {
                "X-CSRFTOKEN": csrftoken,
           },
                processData: false,
                contentType: false,
             // serializes the form's elements.
             beforeSend: function(){
                $('#submit').text('Sending Buy Request...').attr('disabled', true)
            },
               success: function(data)
               {
                document.getElementById('modalhidebutton').click();
                swal("Buy Request Submitted!", "We will get back to you shortly for purchase of "+$("#odoo_product").val()+" version "+$("#odoo_version").val(), "success", {
                  button: "OK",
                }).then((value) => {
                    $('#submit').text('Submit Buy Request').attr('disabled', false)
                    $("#buyformid")[0].reset();
                  });
                // show response from the php script.
               },
               error: function ( xhr, status, error) {
                swal("Server Error", "Please report on info@techneith.com", "error");
              }
             });
      
        
      });
      

});