export function getData(endpoint, callback) {
  const request = new XMLHttpRequest();
  request.onreadystatechange = () => {
    if (request.readyState === 4) {
      callback(request.response);
    }
  };
  request.open("GET", endpoint);
  request.send();
}

export function sendForm(form, action, endpoint, callback) {
  const formData = new FormData(form);
  const dataJSON = JSON.stringify(Object.fromEntries(formData));

  const request = new XMLHttpRequest();
  request.open(action, endpoint);
  request.setRequestHeader("Content-Type", "application/json");

  request.onreadystatechange = () => {
    if (request.readyState === 4) {
      if (request.status >= 200 && request.status < 300) {
        let data;
        try {
          data = JSON.parse(request.responseText);
        } catch {
          data = request.responseText;
        }
        callback(data, form);
      } else {
        console.error("Request failed:", request.status, request.responseText);
        alert("Error: " + request.statusText);
      }
    }
  };

  request.send(dataJSON);
}
