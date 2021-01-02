document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });

/*-------------IMDB API------------------*/  
/*----search------*/
const baseURL = "https://imdb-api.com/API/SearchSeries/APIKEY/"

  
function getData(search, cb) {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", baseURL + search);
    xhr.send();

    xhr.onreadystatechange = function() {

        if (this.readyState == 4 && this.status == 200) {
        
            cb(data = JSON.parse(this.responseText));
        
        }
    };
}

var test = [];

function writeToDocument(search) {
    getData(search, function (data){
        /*clear results*/
        var clear = document.getElementById('data');
        clear.innerHTML = "";
        data = data.results;
        data.forEach(function(searchResult) {
        document.getElementById('data').innerHTML += "<p>" + searchResult.title + "</p>";
        test += searchResult.title
        sessionStorage.setItem("title", test);
        });
        var session = sessionStorage.getItem("title");
    console.log(session)
    })
}

/*------load the correct data---------*/

function b() {
    document.getElementById('test').innerHTML += "<p>" + test + "</p>";
    console.log(test)
}

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