function submitForm() {
    var inputText = document.getElementById("inputText").value;
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "/", true);
    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4 && xhr.status === 200) {
            // handle response from server
            console.log(xhr.responseText);
        }
    };
    xhr.send("inputText=" + encodeURIComponent(inputText));
}

xhr.onreadystatechange = function() {
    if (xhr.readyState === 4 && xhr.status === 200) {
        var response = xhr.responseText;
        var urls = response.split(",");
        var iframe1 = document.createElement("iframe");
        iframe1.src = urls[0];
        document.body.appendChild(iframe1);
        var iframe2 = document.createElement("iframe");
        iframe2.src = urls[1];
        document.body.appendChild(iframe2);
    }
};
