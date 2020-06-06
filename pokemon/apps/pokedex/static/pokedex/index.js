$(document).ready(function(){

    // Load Pokemon Sprites
    for (var i = 1; i < 808; i++){
        $("#pokemons").append('<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/'+i+'.png" id='+i+'>');
    }

    // when image is clicked
    $("img").click(function(){
        pokemonId = this.id;
        sprite = '<img src="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/shiny/'+pokemonId+'.png">';
        $.ajax({
            method: "GET",
            url: "http://pokeapi.co/api/v2/pokemon/" + pokemonId,
            success: function(res){
                var type = "<li>"+res["types"][0]["type"]["name"]+"</li>";
                            
                $("#myModal").modal('show');
                $("#sprite").html(sprite);
                $("#name").html(res["name"]);
                $("#type").html(type);
                $("#height").html(res["height"]);
                $("#weight").html(res["weight"]);
            },
            error: function(){
                alert("Failed");
            }
        });        
    });
});