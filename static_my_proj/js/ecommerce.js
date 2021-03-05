$(document).ready(function(){
    //Contact Form Handler
    var contactForm = $('.contact-form')
    var contactFormMethod = contactForm.attr("method")
    var contactFormEndpoint = contactForm.attr("action")
   
    function displaySubmitting(submitBtn,defaultText,doSubmit){
         if(doSubmit){
        submitBtn.addClass("disabled")
        submitBtn.html("<i class='fa fa-spin fa-spinner'></i>Sending ...")
     }else{
          submitBtn.removeClass("disabled")
          submitBtn.html(defaultText)
     }
   }

    contactForm.submit(function(event){
         event.preventDefault()
         var contactFormSubmitBtn = contactForm.find("[type='submit']")
         var contactFormSubmitBtnTxt = contactFormSubmitBtn.text()
         var contactFormData = contactForm.serialize()
         var thisForm = $(this)
         displaySubmitting(contactFormSubmitBtn," ",true)
         $.ajax({
              method:contactFormMethod,
              url : contactFormEndpoint,
              data :contactFormData,

              success:function(data){
                  thisForm[0].reset()
                  $.alert({
                       title:"Success",
                       content:data.message,
                       theme:"modern",
                  })
                  setTimeout(function(){
                       displaySubmitting(contactFormSubmitBtn,contactFormSubmitBtnTxt,false)
                  },2000)
                 

              },
              error: function(error){
                   console.log(error.responseJSON)
                   var jsonData = error.responseJSON
                   var msg = ""
                   $.each(jsonData, function(key,value){
                        msg+= key+": "+value[0].message + "<br/>"
                   })

                  $.alert({
                       title:"Oops!",
                       content:msg,
                       theme:"modern",
                  })

                  setTimeout(function(){
                       displaySubmitting(contactFormSubmitBtn,contactFormSubmitBtnTxt,false
                       )},2000)
                 

              }

         })
    })

    // Auto Search
     var searchForm = $(".search-form") 
     var searchInput = searchForm.find("[name='q']")
     var typingTimer;
     var typingInterval = 1500 //1.5 seconds
     var searchBtn = searchForm.find("[type='submit']")
     
   //key released
     searchInput.keyup(function(event){
          console.log(event)
          clearTimeout(typingTimer)
          typingTimer = setTimeout(performSearch,typingInterval)
          
     })
     //key pressed
     searchInput.keydown(function(event){
          clearTimeout(typingTimer)
     })
     function displaySearching(){
        searchBtn.addClass("disabled")
        searchBtn.html("<i class='fa fa-spin fa-spinner'></i>Searching ...")
     }
     function performSearch(){
        console.log('BEFORE')
        console.log(window.location.href)
        displaySearching()
        var query = searchInput.val()
        setTimeout(function(){
                        
             window.location.href="http://127.0.0.1:8000/search/?q="+query
             console.log('AFTER')
             console.log(window.location.href)
        },1000)
        

     }
   
   // Cart + Add Products
 var productForm = $(".form-product-ajax") //using a class
   productForm.submit(function(event){
        event.preventDefault();
        console.log("form is not sending")
        var thisForm = $(this) //grabs data related to current form(update_cart).
        //var actionEndpoint = thisForm.attr("action");
        var actionEndpoint = thisForm.attr("data-endpoint");
        var httpMethod = thisForm.attr("method");
        var formData = thisForm.serialize();  
        

        //Ajax Call
        $.ajax({
             url: actionEndpoint,
             method: httpMethod,
             data: formData,
             success: function(data){
                  console.log("success") 
                  console.log(data)
                  console.log("Added", data.added)
                  console.log("Removed",data.removed)
                  var submitSpan = thisForm.find(".submit-span")
                  if (data.added){
                       console.log(submitSpan.html("In cart <button type='submit' class = 'btn btn-link'>Remove</button>"))
                  }else{
                       submitSpan.html("<button class='btn btn-success'>Add to cart</button>")
                  }
                  var navbarCount = $(".navbar-cart-count")
                  navbarCount.text(data.cartItemCount)
                  var currentPath = window.location.href
                  console.log("something",currentPath)
                  if (currentPath.indexOf("cart")!=-1){
                       console.log("function call")
                       refreshCart()
                  }
             },
             error: function(errorData){
                  //JQuery
                  //alert("An error has occurred")

                  
                  //JQuery confirm
                  $.alert({
                       title:"Oops!",
                       content:"An error occured",
                       theme:"modern",
                  })
                  console.log("error")
                  console.log(errorData)
             }
             
             })
        })
        function refreshCart(){
             console.log("in current cart")
             var cartTable = $(".cart-table")
             var cartBody = cartTable.find(".cart-body")
             //cartBody.html("<h1>Changed</h1>")
             var productsRows = cartBody.find(".cart-products")
             var currentUrl = window.location.href
             var refreshCartUrl ='/api/cart/';
             var refreshCartMethod = 'GET';
             var data= {};
             $.ajax({
                  url: refreshCart,
                  method: refreshCartMethod,
                  data: data,
                  success: function(data){
                       console.log(" in cart refresh success")
                       console.log(data)
                       var hiddenCartItemRemoveForm = $('.cart-item-remove-form')
                  
                       if (data.products.length > 0){
                            productsRows.html(" ")
                            i = data.products.length
                            $.each(data.products, function(index, value){
                                 console.log(value)
                                 var newCartItemRemove = hiddenCartItemRemoveForm
                                 newCartItemRemove.css("display","block")
                                 newCartItemRemove.find(".cart-item-product-id").val(value.id)
                                 cartBody.prepend("<tr><th scope='row'>"+ i +"</th><td><a href='"+value.url
                                 +"'>" + value.name +"</a>" + newCartItemRemove.html()+"</td><td>" + value.price + "</td></tr>")
                                 i--
                            })
                            cartBody.find(".cart-subtotal").text(data.subtotal)
                            cartBody.find(".cart-total").text(data.total)

                       } else {
                            window.location.href = currentUrl
                       }
                       
                  },
                  error: function(errorData){
                       console.log("error")
                       console.log(errorData)
                  }
                  
             })
        }
             
        
   })