

function ajaxRequest() {
    const checked = document.getElementById("color-processing").checked;
    console.log("Sending data to the server that the checkbox is", checked);


    const xhr = new XMLHttpRequest();
    xhr.open("POST", "/color-processing");
    xhr.setRequestHeader("Content-Type", "application/json; charset=UTF-8")

    const body = JSON.stringify({
        grayscale: checked,
    });
    xhr.onload = () => {
        if (xhr.readyState == 4 && xhr.status == 201) {
            console.log(JSON.parse(xhr.responseText));
        } else {
            console.log(`Error: ${xhr.status}`);
        }
    };
    xhr.send(body);

}