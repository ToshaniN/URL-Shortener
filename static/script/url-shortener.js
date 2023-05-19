//Function that shortens the provided longURL
function shorten(){
    let givenLongURL = document.getElementsByName("Long URL")[0].value;
    document.getElementsByName("Short URL")[0].value = "";
    //Send request to API with given long URL as parameter. Display shortURL in textbox
    let shortURL;
    let requestURL = new URL('http://127.0.0.1:5000/WantShortURL/');
    requestURL.search = new URLSearchParams({ longURL: givenLongURL });
    fetch(requestURL, { method: 'GET' })
    .then((response) => {
        if (response.ok) {
            console.log("Response ok");
            return response.json();
        } else {
            console.log("Rejecting");
            return Promise.reject(response);
        }
    })
    .then(data => { shortURL = data; })
    .then(() => {document.getElementsByName("Short URL")[0].value = shortURL['returned shortURL'];})
    .catch(err => console.error(err));
    //Enable copy button
    document.getElementById("copy").disabled = false;
}

//Function to retrieve a shortURL's mapped longURL
function retrieve(){
    let givenShortURL = document.getElementsByName("Short URL2")[0].value;
    document.getElementsByName("Long URL2")[0].value = "";
    //Send request to API with given short URL in body. Display longURL in textbox
    let longURL;
    fetch('http://127.0.0.1:5000/WantLongURL/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({"shortURL": givenShortURL})
    })
    // If response is not okay (request fails with 4xx 5xx error) this will reject the promise
    .then((response) => {
        if (response.ok) {
            console.log("Response ok");
            return response.json();
        } else {
            console.log("Rejecting");
            return Promise.reject(response);
        }
    })
    .then(data => { longURL = data; })
    .then(() => {document.getElementsByName("Long URL2")[0].value = longURL['returned longURL'];})
    .catch(err => console.error(err));
    //Enable copy button
    document.getElementById("copy2").disabled = false;
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