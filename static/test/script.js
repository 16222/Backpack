//var xhttp = new XMLHttpRequest();
//xhttp.onreadystatechange =
//primitive get requests
function loadDoc()
{
  var xhttp = new XMLHttpRequest();
  xhttp.open("GET", "/calculation", true);
  xhttp.onreadystatechange = function()
  {
    if(xhttp.readyState === 4 && xhttp.status === 200)
    {
      //alert(xhttp)
      //document.getElementById("test").innerHTML;
      var word = document.getElementById("test").innerHTML;
      alert(word);
      //xhttp.open("POST", "")
    }
  }
  xhttp.send();
}
//primitive fetch request
function loadDoc()
{
  $("#weapon").change(function(){
    var weapon  = $("#weapon").val();
    fetch("/calculation").then(function(response){
      $("#AS").text("weaponData[1]");
    })
  }
)}

//primitive text changing
function getTextTest(){
  var word = $("#AS").text();
  alert(word);
}

//primitive getting results from route
function getWeaponId(){
  var weapon = $("#weapon").text();
  alert(weapon)
}
