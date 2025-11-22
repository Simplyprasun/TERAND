# TERAND
**Restaurant Menu & Feedback System**
**(Flask + Python + CSV Project)**

This project is a Flask-powered restaurant menu website that displays a list of dishes from a CSV file, highlights the highest-rated dish, and allows users to submit feedback and star ratings.
Every submitted rating is stored in a per-dish list, and the average rating is automatically updated in the CSV file.

**Features**
1. Menu Display Page

Reads menu data from menu.csv

Shows:

-> Dish ID

-> Dish Name

-> Price

-> Rating

-> Displays a Highly Rated Dish in a separate highlighted box

-> A glowing "Give Feedback" button redirects to a feedback page

2. Feedback Page

-> Dropdown of all dish names

-> 5-star rating input

-> Feedback text box

-> On submission:
✔ Rating stored in a separate per-dish list
✔ New average rating calculated
✔ CSV updated with new rating
✔ Redirects to Thank You Page

3. Thank You Page

Displays:

Thank you for your valuable feedback.

4. Rating Logic Explained
-> When a user submits a rating:

-> New rating appended to the dish’s list

-> Average rating recalculated

-> CSV file updated

-> Highest-rated dish recalculated on every page load

5. Technologies Used

-> Flask (Python backend framework)

-> Python CSV module

-> HTML5 / CSS3 (Glass morphism + gradients)

-> JavaScript (Particle animations + glow effects)

-> CSV file as database for menu + ratings
