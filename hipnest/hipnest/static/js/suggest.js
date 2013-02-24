/*
 * javascript file for search bar
 */
var bands = ['Goldfish', 'RJD2', 'Queen']
$('#searchbar').typeahead({source:bands})

$(document).ready(function(){
    var rating = 0.5
    $('#left_button').click(function(){
	rating = rating - 0.1;
	$('#artist_info').hide("slide", {direction: "left"}, 1000, function(){
	    $('#artist_info').html("CHANGED!  " + rating);
	    $('#artist_info').show("slide", {direction: "right"}, 1000);
	});
    });

    $('#right_button').click(function(){
	 rating = rating + 0.1;
	$('#artist_info').hide("slide", {direction: "right"}, 1000, function(){
	    $('#artist_info').html("CHANGED!  " + rating);
	    $('#artist_info').show("slide", {direction: "left"}, 1000);
	});
		
    });

    
});