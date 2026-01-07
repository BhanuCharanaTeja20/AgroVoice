from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/sell", methods=["GET", "POST"])
def sell():
    message = None

    if request.method == "POST":
        crop = request.form["crop"]
        quantity = request.form["quantity"]
        price = request.form["price"]
        message = f"Crop Listed Successfully: {crop}, {quantity} kg at ₹{price}/kg"

    return render_template("sell.html", message=message)


@app.route("/buy")
def buy():
    return render_template("buy.html")


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


@app.route("/markets")
def markets():
    return render_template("markets.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)