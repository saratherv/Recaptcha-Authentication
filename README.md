# Recaptcha-Authentication

# Backend:
- built using python and flask framework and MongoDB as a database is used

# Frontend:
- Built using Semantic UI and JS & jQuery with AJAX is used for calling Backend API.

# Server:
- used ngrok as local tunnel and ngrok url is added to domains in google recaptcha API.
# To run this app:
- clone the repository
- cd Recaptcha-Authentication
- pip install requirements.txt
- open another terminal and run ngrok using ./ngrok http 5000
- python app.py
- add ngrok https url to google recaptacha console domains
- update ngrok url in static/js/captcha.js file
