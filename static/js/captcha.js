$(document).ready(function(){
    $('.recaptchaForm').on('submit' , function(event){
        var recap = $('#g-recaptcha-response').val();
        console.log(recap)
        console.log('hello')
        if(recap === ""){
            event.preventDefault();
            alert('please check recaptcha')
        }
        if(recap == undefined)
          recap = null
        event.preventDefault();
       var ip = document.getElementById('ip').innerHTML
       var username = document.getElementById('username').value
       var email = document.getElementById('email').value
       var password = document.getElementById('password').value
     $.ajax({ 
           type:"POST",
           url:"https://88fec1ce.ngrok.io/add",
           data: JSON.stringify({'token' : recap, "ip" : ip, 'username' :username,'email':email, 'password':password}), 
           contentType: 'application/json',
           success: function(res) {
                   console.log(res);
                   if(res == true){
                       addCaptcha();
                   }
                   if(res!= null && res!=true){
                       addResult(res)
                   }
                   console.log("Added");
           }.bind(this),
           error: function(xhr, status, err) {
                   console.error(xhr, status, err.toString());
           }.bind(this)
           });
       })

   })
   function addCaptcha(){
      onloadCallback()
   }
   function addResult(res){
       document.getElementById('result').innerHTML = res
   }