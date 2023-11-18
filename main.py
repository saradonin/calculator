from flask import Flask, request, render_template
from models import Bottle

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
def calculate_volume():
    if request.method == "GET":
        return render_template("calculator_form.html")
    else:
        try:
            initial_volume = float(request.form.get("initial_volume",0))
            initial_weight = float(request.form.get("initial_weight",0))
            current_weight = float(request.form.get("current_weight",0))
            density = float(request.form.get("density",0.84))
            current_volume = round(Bottle.calculate_current_volume(
                initial_volume,
                initial_weight,
                current_weight,
                density
            ), 2)
            
            return render_template("calculator_form.html", 
                                current_volume=str(current_volume)+" ml", 
                                initial_volume=initial_volume, 
                                initial_weight=initial_weight,
                                current_weight=current_weight,
                                density=density)
        except ValueError:
            message = "Please fill in all fields correctly."
            return render_template("calculator_form.html", message=message)


if __name__ == "__main__":
    app.run(debug=True, port=5001)