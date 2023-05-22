

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


$('#contact_form').on('submit', function(e) {

    e.preventDefault(); // avoid to execute the actual submit of the form.
    

   
    
    var form = $(this);
    var url = base_url+"/contact/";
    var fd = new FormData();    
    var csrftoken = getCookie('csrftoken');
    fd.append('email',$("#email").val())
    fd.append('name',$("#name").val())
    fd.append('description',$("#description").val())
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
         
            $('#submit').text('Please Wait...').attr('disabled', true).addClass('bt-hud');
  
            
           
        },
           success: function(data)
           {
            swal("Thank You", "Thanks for reaching out! Shortly will contact you.", "success").then((value) => {
                $('#submit').text('Submit').attr('disabled', false).removeClass('bt-hud')
                $("#contact_form")[0].reset();
              });
            // show response from the php script.
           },
           error: function ( xhr, status, error) {
            swal("Server Error", "Please report on info@techneith.com", "error");
          }
         });

    
});
});