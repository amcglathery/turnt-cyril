/*
 * javascript file for search bar
 */


function transform_rating($r){
    var n = Math.ceil(($r - 0.1) * 10) - 4; 
    console.log($r + " " + n);
    return n;
}


$(document).ready(function(){
    var comments = new Array();
    comments[0] = "Really, really, really under the radar";
    comments[1] = "Starting to get popular";
    comments[2] = "Getting up the popularity totem pole";
    comments[3] = "Has a potential to be the next big thing";
    comments[4] = "Sooner or later, this artist will be everywhere";
    comments[5] = "We eat, breathe, and sleep this artist's music";

    var rating = 0.7;
    $('#snarky_comment').html(comments[2])
    $('#left_button').click(function(){
	rating = rating - 0.1;
	$('#snarky_comment').html(comments[transform_rating(rating)]);

	$('#artist_info').hide("slide", {direction: "left"}, 1000, function(){
	    $('#artist_info').html("CHANGED!  " + rating);
	    $('#artist_info').show("slide", {direction: "right"}, 1000);
	});
    });

    $('#right_button').click(function(){
	 rating = rating + 0.1;
	$('#snarky_comment').html(comments[transform_rating(rating)]);
	$('#artist_info').hide("slide", {direction: "right"}, 1000, function(){
	    $('#artist_info').html("CHANGED!  " + rating);
	    $('#artist_info').show("slide", {direction: "left"}, 1000);
	});
		
    });
    
});
