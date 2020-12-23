document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.sidenav');
    var instances = M.Sidenav.init(elems, {});
  });

/*-------------IMDB API------------------*/  
const baseURL = "https://imdb-api.com/API/SearchSeries/k_y8kd93un/"
  
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

function writeToDocument(search) {
    getData(search, function (data){
        /*clear results*/
        var clear = document.getElementById('data');
        clear.innerHTML = "";
        data = data.results;
        data.forEach(function(searchResult) {
        document.getElementById('data').innerHTML += "<p>" + searchResult.title + "</p>";
        });
        
    })
}