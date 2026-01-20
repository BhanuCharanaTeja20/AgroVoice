from flask import Flask, render_template, request

app = Flask(__name__)

# ---------------- HOME ----------------
@app.route("/")
def home():
    return render_template("index.html")


# ---------------- DISEASE LIST ----------------
@app.route("/diseases")
def diseases():
    return render_template("diseases.html")


# ---------------- SOLUTION PAGE ----------------
@app.route("/solution/<disease_id>")
def solution(disease_id):

    data = {
        "tomato_early": {
            "disease": "Tomato Early Blight",
            "symptoms": "Brown spots on leaves",
            "solution": "Use fungicide and remove infected leaves",
            "prevention": "Crop rotation",
            "brands": [
                "Dithane M-45 (UPL)",
                "Kavach (Syngenta)",
                "Indofil M-45"
            ]
        },

        "tomato_late": {
            "disease": "Tomato Late Blight",
            "symptoms": "Dark patches, leaf decay",
            "solution": "Apply copper fungicide",
            "prevention": "Avoid overhead irrigation",
            "brands": [
                "Ridomil Gold (Syngenta)",
                "Curzate (DuPont)"
            ]
        },

        "rice_brown": {
            "disease": "Rice Brown Spot",
            "symptoms": "Brown lesions on leaves",
            "solution": "Apply systemic fungicide",
            "prevention": "Balanced fertilization",
            "brands": [
                "Bavistin (BASF)",
                "Saaf (UPL)"
            ]
        },

        "rice_blast": {
            "disease": "Rice Leaf Blast",
            "symptoms": "Diamond-shaped spots",
            "solution": "Use blast-resistant varieties",
            "prevention": "Proper water management",
            "brands": [
                "Nativo (Bayer)",
                "Tricyclazole"
            ]
        }
    }

    info = data.get(disease_id)

    if not info:
        return "Disease not found"

    return render_template("solution.html", info=info)


# ---------------- SELL ----------------
@app.route("/sell", methods=["GET", "POST"])
def sell():
    message = None

    if request.method == "POST":
        crop = request.form["crop"]
        quantity = request.form["quantity"]
        price = request.form["price"]

        message = f"Crop Listed Successfully: {crop}, {quantity} kg at ₹{price}/kg"

    return render_template("sell.html", message=message)


# ---------------- BUY ----------------
@app.route("/buy")
def buy():
    return render_template("buy.html")


# ---------------- RECOMMEND ----------------
@app.route("/recommend", methods=["GET", "POST"])
def recommend():
    crops = []

    if request.method == "POST":
        season = request.form["season"]
        soil = request.form["soil"]

        if season == "Kharif" and soil == "Black":
            crops = ["Cotton", "Soybean", "Maize"]
        elif season == "Rabi" and soil == "Loamy":
            crops = ["Wheat", "Mustard", "Gram"]
        elif season == "Summer" and soil == "Sandy":
            crops = ["Watermelon", "Cucumber", "Groundnut"]
        else:
            crops = ["Rice", "Millets", "Pulses"]

    return render_template("recommend.html", crops=crops)


# ---------------- MARKETS ----------------
@app.route("/markets")
def markets():
    return render_template("markets.html")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    app.run(debug=True)