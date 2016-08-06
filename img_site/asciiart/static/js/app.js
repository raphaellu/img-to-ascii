  // initialize the boostrap file picker
  $('input[type=file]').bootstrapFileInput();
  $('.file-inputs').bootstrapFileInput();

  $(document).ready(
    // enable the submit button only after file has been uploaded
    function(){ $('input:file').change( function(){
        if ($(this).val()) {
            $('input:submit').attr('disabled',false);
        } 
      }
    );
  // taiji button onclick
  $("#taiji").click(function(e){
      $("#taiji").toggleClass("rotateTaiji");
      e.preventDefault();
        $.ajax({
          type:"POST",
          url:"/toggle_color",
          success: function(data){
            $(".prettyprint").html(data); // reverse ascii art's  color
          }
      });
  })

  $("#welcome").typed({
        strings: ["Welcome to Ascii Art !","Simply upload an image :D"],
        typeSpeed: 0
      });

  });

// acquire the csrftoken 
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
var csrftoken = getCookie('csrftoken');

// set the header on AJAX request
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
