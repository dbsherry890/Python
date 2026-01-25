from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    return render_template_string("""
    <!doctype html>
    <html>
    <body>
      <h1>Flask + JS Demo</h1>
      <form id="greetForm">
        <input id="nameInput" name="name" placeholder="Enter your name">
        <button type="submit">Submit</button>
      </form>
      <div id="result"></div>
      
      <script>
        const form = document.querySelector("#greetForm");
        form.addEventListener("submit", (e) => {
          e.preventDefault();  // stop page reload
          
          const name = document.querySelector("#nameInput").value;
          fetch("/greet?name=" + encodeURIComponent(name))
            .then(res => res.json())
            .then(data => {
              document.querySelector("#result").textContent = data.message;
            });
        });
      </script>
    </body>
    </html>
    """)


@app.route("/greet")
def greet():
    name = request.args.get("name", "Stranger")
    return jsonify({"message": f"Hello, {name}!"})


if __name__ == "__main__":
    app.run(debug=True)
