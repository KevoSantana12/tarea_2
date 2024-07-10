from flask import request, render_template, redirect, url_for, current_app as app

from business import BusinessLogic
from Entities import Cambio_dto


business_logic = BusinessLogic()

@app.route('/')
def home():
    return render_template('index.html')