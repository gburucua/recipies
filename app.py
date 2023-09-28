from flask import Flask, request, render_template, jsonify
import requests
import json

app = Flask(__name__)

def get_recipe_suggestions(ingredients):
    # Spoonacular API endpoint and API key (replace with your own)
    api_endpoint = "https://api.spoonacular.com/recipes/findByIngredients"
    api_key = "0107042399844409a4dee2b37094cf11"

    params = {
        "apiKey": api_key,
        "ingredients": ",".join(ingredients),
        "number": 5
    }

    try:
        response = requests.get(api_endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except requests.exceptions.RequestException as e:
        print("Error:", str(e))
        return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        ingredients = request.form.get("ingredients")
        if ingredients:
            ingredients_list = ingredients.split(",")
            recipe_suggestions = get_recipe_suggestions(ingredients_list)
            return render_template("index.html", recipe_suggestions=recipe_suggestions)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
