from flask import Blueprint, render_template, request

from venues.service.venues_selector import VenuesSelector
from venues.context import feed_data
from venues.server.forms import UsersForm

services = Blueprint('services', __name__)


@services.route('/', methods=['GET', 'POST'])
def hello_world():
    users_form = UsersForm(request.form)
    venues = VenuesSelector(feed_data())
    users_form.users_select.choices = zip(venues.get_user_names(), venues.get_user_names())
    if request.method == 'POST' and users_form.validate():
        selected_venues = venues.select_venues(users_form.users_select.data)
        return render_template("venues.html", venues=selected_venues, users=users_form.users_select.data)
    else:
        return render_template("users_form.html", form=users_form)