$(document).ready(function(){

    $("#login_button").click(function(e){
        e.preventDefault();
        var data = $("#login_form").serialize();

        $.ajax({
            method: "POST",
            url: "/login",
            data: data,
            success: function(res){
                window.location = "/pokedex"
            },
            error: function(){
                alert("Something went wrong")
            }        
        });
    });

    $("#register_button").click(function(e){
        e.preventDefault();
        
        var data = $("#register_form").serialize();

        $.ajax({
            method: "POST",
            url: "/register",
            data: data,
            success: function(res){
                window.location = "/"                
            },
            error: function(){
                alert("Something went wrong")
            }        
        });
    });
}); 