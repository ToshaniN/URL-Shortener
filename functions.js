//Function that adds text to short URL box when button is clicked
var howManyURLs = 0;
function shorten(){
    document.getElementsByName("Short URL")[0].value = "";
    document.getElementsByName("Short URL")[0].value = "https://urlshortener.com/Token" + howManyURLs;
    document.getElementById("copy").disabled = false;
    localStorage.setItem(document.getElementsByName("Short URL")[0].value, document.getElementsByName("Long URL")[0].value);
    howManyURLs++;
}

//Function to copy the produced URLs
function copyToClipboard(urlName){
    if (urlName == 'copy') {
        var url = document.getElementById("Short URL");
    } else {
        var url = document.getElementById("Long URL2");
    }                
    url.select();
    navigator.clipboard.writeText(url.value);
    //alert("Short URL copied successfully");
}

//Function to retrieve a short URL's mapped long URL
function retrieve(){
    var longURL = localStorage.getItem(document.getElementsByName("Short URL2")[0].value);
    document.getElementsByName("Long URL2")[0].value = "";
    document.getElementsByName("Long URL2")[0].value = longURL;
    document.getElementById("copy2").disabled = false;
}

// function clear(urlId) {
//     alert("Made it here1");
//     if (urlId == 'Long URL') {
//         alert("Made it here2");
//         document.getElementsByName("Long URL")[0].value = "";
//         alert("Made it here2");
//     } else {
//         document.getElementsByName("Short URL2")[0].value = "";
//     }

// }

//Checks if URL is valid, and enables button if yes, disables if invalid, clears returned URL on any changes
const enteredURL = document.getElementById("Long URL");
enteredURL.addEventListener("input", (event) => {
    const isValid = event.target.checkValidity();
    if (isValid) {
        document.getElementById("generate").disabled = false;
    } else {
        document.getElementById("generate").disabled = true;
    }
    document.getElementById("Short URL").value = "";
    document.getElementById("copy").disabled = true;
});

const enteredURL2 = document.getElementById("Short URL2");
enteredURL2.addEventListener("input", (event) => {
    const isValid = event.target.checkValidity();
    if (isValid) {
        document.getElementById("retrieve").disabled = false;
    } else {
        document.getElementById("retrieve").disabled = true;
    }
    document.getElementById("Long URL2").value = "";
    document.getElementById("copy2").disabled = true;
});