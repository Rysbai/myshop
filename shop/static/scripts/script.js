// using jQuery
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



$("#btn-addtocart").click( function(){
  $.ajax({
    type: "POST",
    url: $('#cart-form')[0].action,
    data: {
      "quantity" : $("#id_quantity option:selected").val(),
      "update": false
    },
    dataType: "json",
    success: function (data) {
        console.log(data)
        if(data['get_total_price'] > 0) {
          $("#total_item").html("Корзина: " + data['get_total_price'] + " сом.");
        }
        else {
          $("#total_item").html("Корзина пуста");
        }
      }
  });
});

// $("#list-btn-addtocart").click( function() {
//   $.ajax({
//     type: "POST",
//     url: $("#cart-form")[0].action,
//     data: {
//       "quantity": 1,
//       "update": false,
//     },
//     dataType: "json",
//     success: function (data){
//       $("#total_item").html("Корзина: " + data['get_total_price'] + " сом.");
//       console.log("Hi")
//     }
//   })
// })
// $("#get_cupon").click( function(){
//   $.ajax({
//     type: "POST",
//     url: $("#cupon_form")[0].action,
//     data: {
//       "code" : $("#id_code").val()
//     },
//     dataType: "json",
//     success: function (data) {
//       console.log(data);
//       $("#cupon-title").text("Сумма без скидки: ")
//       $("#get_total_price").text(float(data["get_total_price"]) + " сом.")
//       $("#cupon-info").text('"' + data["code"] + '" купон на (' + float(data["cupon_discount"]) + ') % ниже.')
//       $("#discount").text(" - " + float(data["get_discount"]) + " сом.")
//       $("#get_total_price_after_discount").text(float(data["get_total_price_after_discount"]) + " сом.")
//     }
//   });
// });
