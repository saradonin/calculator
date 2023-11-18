from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def calculate_volume():
    if request.method == "GET":
        return render_template("calculator_form.html", density=0.84)
    else:
        try:
            initial_volume = float(request.form.get("initial_volume"))
            initial_weight = float(request.form.get("initial_weight"))
            current_weight = float(request.form.get("current_weight"))
            density = float(request.form.get("density"))

            current_volume = round(
                initial_volume - ((initial_weight - current_weight) / density), 2)

            return render_template("calculator_form.html",
                                   current_volume=current_volume,
                                   initial_volume=initial_volume,
                                   initial_weight=initial_weight,
                                   current_weight=current_weight,
                                   density=density)
        except ValueError:
            message = "Please fill in all fields correctly."
            return render_template("calculator_form.html", message=message)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
