from flask import Flask, render_template, request, redirect

app = Flask(__name__)

helados = [
    {"id": 1, "sabor": "Chocolate", "precio": 10},
    {"id": 2, "sabor": "Vainilla", "precio": 9},
    {"id": 3, "sabor": "Fresa", "precio": 11},
]

pedidos = []

@app.route("/")
def index():
    return render_template("index.html", helados=helados, pedidos=pedidos)

@app.route("/ordenar", methods=["POST"])
def ordenar():
    sabor_id = int(request.form.get("sabor"))
    helado = next((h for h in helados if h["id"] == sabor_id), None)
    if helado:
        pedidos.append({"sabor": helado["sabor"], "precio": helado["precio"]})
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
