#!/usr/bin/python3
"""
Flask App that integrates with AirBnB static HTML Template
"""
import uuid
from flask import Flask, render_template
from models import storage

# flask setup
app = Flask(__name__)
app.url_map.strict_slashes = False


# begin flask page rendering
@app.teardown_appcontext
def teardown_db(exception):
    """
    after each request, this method calls .close() (i.e. .remove()) on
    the current SQLAlchemy Session
    """
    storage.close()


@app.route("/1-hbnb")
def hbnb_filters(the_id=None):
    """
    handles request to custom template with states, cities & amentities
    """
    state_objs = storage.all("State").values()
    states = dict([state.name, state] for state in state_objs)
    amens = storage.all("Amenity").values()
    places = storage.all("Place").values()
    users = dict(
        [user.id, "{} {}".format(user.first_name, user.last_name)]
        for user in storage.all("User").values()
    )
    cache_id = str(uuid.uuid4())
    return render_template(
        "1-hbnb.html",
        states=states,
        amens=amens,
        places=places,
        users=users,
        cache_id=cache_id,
    )


if __name__ == "__main__":
    """
    MAIN Flask App"""
    app.run(host="0.0.0.0", port=5001)
