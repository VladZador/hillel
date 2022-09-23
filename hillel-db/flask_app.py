from flask import Flask, request

from utils import get_filtered_customers, get_number_of_customer_names, get_total_profit

app = Flask(__name__)


@app.route("/")
def hello():
    greeting_text = "Hello! There's nothing interesting on this page. " \
        "To get clients, filtered by city and/or state (if necessary), go to <b>/filter</b>. " \
        "To get the numbers of occurrences of names in the database, go to <b>/names</b>. " \
        "To get the orders profit, go to <b>/profit</b>"
    return greeting_text


@app.route("/filter", methods=["GET"])
def show_filtered_customers():
    city = request.args.get("city", default=None)
    state = request.args.get("state", default=None)
    result = get_filtered_customers(city, state)
    return result


@app.route("/names")
def show_number_of_customer_names():
    return get_number_of_customer_names()


@app.route("/profit")
def show_total_profit():
    return "Total profit is " + get_total_profit()
