const { data } = require("./data");

const query = 'How many 3 bedroom homes are there?'

const requestData = {data, query}

async function postData(url = "", data = {}) {
    const response = await fetch(url, {
      method: "POST", 
      mode: "cors", 
      cache: "no-cache", 
      credentials: "same-origin", 
      headers: {
        "Content-Type": "application/json",
      },
      redirect: "follow", 
      referrerPolicy: "no-referrer", 
      body: JSON.stringify(data),
    });
    return response.json();
}

reqUrl = "http://127.0.0.1:5000/queryJson"
postData(reqUrl, requestData).then((data) => {
  console.log(data); 
});