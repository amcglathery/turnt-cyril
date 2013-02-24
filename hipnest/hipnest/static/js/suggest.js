/*
 * javascript file for search bar
 */
var bands = ['Goldfish', 'RJD2', 'Queen']
$('#searchbar').typeahead({source:bands})

$(document).ready(function(){
    $('#left_button').click(function(){
	alert('hiiiii');
	$('#a_id').hide("slide", {direction: "left"}, 1000, function(){
	    $('#a_id').html("CHANGED!");
	    $('#a_id').show("slide", {direction: "right"}, 1000);
	});
	
	
    });
    
});