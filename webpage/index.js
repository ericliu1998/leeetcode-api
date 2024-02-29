document.getElementById("dl").addEventListener("click", generatefiles);

function generatefiles() {
  console.log("generate files clicked");

  const url2 = getCurrentTabUrl();
  url2.then((url) => {
    document.querySelector("#msg").textContent = JSON.stringify(url) + "\n";
    const urlArr = url.split("/");
    console.log(urlArr);

    let getUrl = "http://127.0.0.1:8000/generate-files/" + urlArr[4];

    fetch(getUrl)
      .then((response) => response.json())
      .then((json) => {
        console.log(json);
        document.querySelector("#msg").textContent += json.status;
      })
      .catch((error) => {
        console.log(error);
      });
  });
}
document
  .getElementById("solutionfile")
  .addEventListener("click", dlSolutionFile);

function dlSolutionFile() {
  console.log("solutionfile clicked");
  url = "http://127.0.0.1:8000/getSolutionFile";
  window.open(url);
}

document.getElementById("testfile").addEventListener("click", dlTestFile);

function dlTestFile() {
  console.log("testfile clicked");
  url = "http://127.0.0.1:8000/getTestFile";
  window.open(url);
}

document.getElementById("printurl").addEventListener("click", printUrl);

function printUrl() {
  console.log("print url");
  const url2 = getCurrentTabUrl();
  url2.then((url) => {
    document.querySelector("#msg").textContent = JSON.stringify(url) + "\n";
  });
}

async function getCurrentTabUrl() {
  let queryOptions = { active: true, currentWindow: true };
  // `tab` will either be a `tabs.Tab` instance or `undefined`.
  let tab = await chrome.tabs.query(queryOptions);

  return tab[0].url;
}

document.getElementById("testurl").addEventListener("click", testUrl);
function testUrl() {
  const promise = getCurrentTabUrl();
  promise.then((data) => {
    document.querySelector("#msg").textContent = JSON.stringify(data) + "\n";
    console.log(data);
  });
}
printUrl();
