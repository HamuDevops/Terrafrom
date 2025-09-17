from flask import Flask, render_template_string

app = Flask(__name__)

# Sample vegetable data
vegetables = [
    {"name": "Carrots", "price": "₹40/kg", "image": "🥕"},
    {"name": "Tomatoes", "price": "₹30/kg", "image": "🍅"},
    {"name": "Spinach", "price": "₹25/bunch", "image": "🥬"},
    {"name": "Corn", "price": "₹50/kg", "image": "🌽"},
]

@app.route("/")
def home():
    html = """
    <html>
        <head>
            <title>Farmer's Fresh Veggies</title>
            <style>
                body { font-family: Arial; background-color: #f0fff0; text-align: center; }
                h1 { color: #228B22; }
                .veggie { margin: 20px; padding: 10px; border: 1px solid #ccc; display: inline-block; background: #fff; border-radius: 10px; width: 200px; }
            </style>
        </head>
        <body>
            <h1>🌾 Welcome to Farmer Hamu's Veggie Market 🌾</h1>
            <p>Fresh from the farm, straight to your kitchen!</p>
            {% for veg in vegetables %}
                <div class="veggie">
                    <h2>{{ veg.image }} {{ veg.name }}</h2>
                    <p><strong>Price:</strong> {{ veg.price }}</p>
                </div>
            {% endfor %}
        </body>
    </html>
    """
    return render_template_string(html, vegetables=vegetables)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
