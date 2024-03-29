
let HEADER = {
    "Content-Type": "application/json",
    "Accept": "application/json",
}

function test_button(){
    let body = {
        "msg":"12345"
    }
    console.log(JSON.stringify(body));
    fetch('/test/', {method: "POST",headers:HEADER, body:JSON.stringify(body)})
    .then((response) => {
        console.log(response)
        return response.json(); // 可以透過 blob(), json(), text() 轉成可用的資訊
    })
    .then((jsonData) => {
        console.log(jsonData);
    });
}