//Function that adds text to short URL box when button is clicked
let howManyURLs = 0;
let longToShort = Object.fromEntries(Object.entries(localStorage).map(([key,value]) => [value,key]));

function shorten(){
    //Check last created URL, and make unique token accordingly
    let longURL = document.getElementsByName("Long URL")[0].value;
    let sortedKeys = Object.keys(localStorage).sort();
    let lastURL = "";
    if (sortedKeys.length != 0) {
        lastURL = sortedKeys[sortedKeys.length - 1];
        howManyURLs = parseInt(lastURL.substring(30)) + 1; //30 is index after https...Token
    }
    let shortURL = "https://urlshortener.com/Token" + howManyURLs;

    //Check if long url has already been shortened, return mapped short url if yes
    if (longToShort.hasOwnProperty(longURL)) {
            shortURL = longToShort[longURL];
    } else {
        longToShort[longURL] = shortURL;
        console.log(longToShort);
    }

    //Set short URL value to what was found/calculated above 
    document.getElementsByName("Short URL")[0].value = "";
    document.getElementsByName("Short URL")[0].value = shortURL;
    document.getElementById("copy").disabled = false;
    localStorage.setItem(shortURL, longURL);
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
}

//Function to retrieve a short URL's mapped long URL
function retrieve(){
    let longURL = localStorage.getItem(document.getElementsByName("Short URL2")[0].value);
    document.getElementsByName("Long URL2")[0].value = "";
    document.getElementsByName("Long URL2")[0].value = longURL;
    document.getElementById("copy2").disabled = false;
}

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