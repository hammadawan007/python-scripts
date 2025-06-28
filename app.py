from flask import Flask, render_template, request, redirect, url_for, session
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Sample Laptop Items
items = [
    {
        "id": 1,
        "name": "Dell XPS 13",
        "price": 1200,
        "image": "https://images.pexels.com/photos/374074/pexels-photo-374074.jpeg"
    },
    {
        "id": 2,
        "name": "MacBook Pro",
        "price": 2500,
        "image": "https://images.pexels.com/photos/18105/pexels-photo.jpg"
    },
    {
        "id": 3,
        "name": "Lenovo ThinkPad",
        "price": 999,
        "image": "https://images.pexels.com/photos/1181308/pexels-photo-1181308.jpeg"
    }
]



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/items')
def show_items():
    return render_template('items.html', items=items)

@app.route('/add-to-cart/<int:item_id>')
def add_to_cart(item_id):
    if 'cart' not in session:
        session['cart'] = []
    for item in items:
        if item['id'] == item_id:
            session['cart'].append(item)
            break
    return redirect(url_for('show_cart'))

@app.route('/cart')
def show_cart():
    cart = session.get('cart', [])
    total = sum(item['price'] for item in cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Simulated payment logic
        card_number = request.form['card_number']
        if card_number.startswith("4"):  # dummy VISA validation
            session.pop('cart', None)
            return render_template('checkout.html', message="Payment Successful!")
        else:
            return render_template('checkout.html', message="Payment Failed!")
    return render_template('checkout.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/feedback', methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        print(f"Feedback Received:\nName: {name}\nEmail: {email}\nMessage: {message}")
    return render_template('feedback.html', page='feedback')


if __name__ == '__main__':
    app.run(host="any", port=5000, debug=True)
