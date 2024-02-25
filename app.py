from flask import Flask, render_template, request

app = Flask(__name__)

# Sample data to search from
data = ["Apple", "Banana", "Cherry", "Date", "Elderberry", "Fig", "Grape"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    # Filter the data based on the query
    results = [item for item in data if query in item.lower()]
    return render_template("partials/search_results.html", results=results)

if __name__ == "__main__":
    app.run(debug=True)
