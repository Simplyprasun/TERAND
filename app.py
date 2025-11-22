from flask import Flask, render_template, request, redirect, url_for
import csv
import os


app = Flask(__name__)
MENU_CSV = os.path.join(os.path.dirname(__file__), "menu.csv")


# In-memory ratings lists for each dish
ratings_db = {} # { dish_name: [ratings...] }
def load_menu():
    menu = []
    if not os.path.exists(MENU_CSV):
        return menu
    with open(MENU_CSV, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # convert types
            row['price'] = float(row['price'])
            row['rating'] = float(row['rating'])
            menu.append(row)
    return menu
def save_menu(menu):
    fieldnames = ['dish_id', 'dish_name', 'price', 'rating']
    with open(MENU_CSV, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in menu:
            # ensure rating saved as float with 2 decimals
            writer.writerow({
            'dish_id': r['dish_id'],
            'dish_name': r['dish_name'],
            'price': r['price'],
            'rating': f"{float(r['rating']):.2f}"
            })
@app.route('/')
def home():
    menu = load_menu()
    # ensure every dish has a list in ratings_db
    for item in menu:
        if item['dish_name'] not in ratings_db:
            # initialize with the current rating (so averages start meaningful)
            ratings_db[item['dish_name']] = [int(round(item['rating']))] if item['rating']>0 else []


            # top rated dish by rating column (tie-breaker: first)
            top_dish = None
            if menu:
                top_dish = max(menu, key=lambda x: x['rating'])
            return render_template('home.html', menu=menu, top_dish=top_dish)
@app.route('/feedback')
def feedback():
    menu = load_menu()
    dishes = [d['dish_name'] for d in menu]
    return render_template('feedback.html', dishes=dishes)
@app.route('/submit_feedback', methods=['POST'])
def submit_feedback():
    dish = request.form.get('dish_name')
    rating = int(request.form.get('rating', 5))
    text = request.form.get('text_feedback', '')
    # append rating to in-memory list
    if dish not in ratings_db:
        ratings_db[dish] = []
    ratings_db[dish].append(rating)

    # update CSV average rating for that dish
    menu = load_menu()
    for item in menu:
        if item['dish_name'] == dish:
            avg = sum(ratings_db[dish]) / len(ratings_db[dish])
            item['rating'] = avg
    save_menu(menu)

    # you could store text feedback to a file/db — omitted here per spec
    return redirect(url_for('thankyou'))
@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)