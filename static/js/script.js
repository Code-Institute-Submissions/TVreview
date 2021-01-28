document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });

/*---------star rating----------*/

function starChange1() {
    document.getElementById("star-rating1").innerHTML = "star";
}

function star1() {
    document.getElementById("star-rating1").innerHTML = "star_border";
}

function starChange2() {
    document.getElementById("star-rating1").innerHTML = "star";    
    document.getElementById("star-rating2").innerHTML = "star";
}

function star2() {
    document.getElementById("star-rating1").innerHTML = "star_border";
    document.getElementById("star-rating2").innerHTML = "star_border";
}

function starChange3() {
    document.getElementById("star-rating1").innerHTML = "star";    
    document.getElementById("star-rating2").innerHTML = "star";
    document.getElementById("star-rating3").innerHTML = "star";
}

function star3() {
    document.getElementById("star-rating1").innerHTML = "star_border";
    document.getElementById("star-rating2").innerHTML = "star_border";
    document.getElementById("star-rating3").innerHTML = "star_border";
}

function starChange4() {
    document.getElementById("star-rating1").innerHTML = "star";    
    document.getElementById("star-rating2").innerHTML = "star";
    document.getElementById("star-rating3").innerHTML = "star";
    document.getElementById("star-rating4").innerHTML = "star";
}

function star4() {
    document.getElementById("star-rating1").innerHTML = "star_border";
    document.getElementById("star-rating2").innerHTML = "star_border";
    document.getElementById("star-rating3").innerHTML = "star_border";
    document.getElementById("star-rating4").innerHTML = "star_border";
}

function starChange5() {
    document.getElementById("star-rating1").innerHTML = "star";    
    document.getElementById("star-rating2").innerHTML = "star";
    document.getElementById("star-rating3").innerHTML = "star";
    document.getElementById("star-rating4").innerHTML = "star";
    document.getElementById("star-rating5").innerHTML = "star";
}

function star5() {
    document.getElementById("star-rating1").innerHTML = "star_border";
    document.getElementById("star-rating2").innerHTML = "star_border";
    document.getElementById("star-rating3").innerHTML = "star_border";
    document.getElementById("star-rating4").innerHTML = "star_border";
    document.getElementById("star-rating5").innerHTML = "star_border";
}


/*----------favourite----------*/

function favoriteChange() {
    document.getElementById("favorite").innerHTML = "favorite";
}

function favorite() {
    document.getElementById("favorite").innerHTML = "favorite_border";
}