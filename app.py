from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
import requests
from form import MovieForm, AddMovie

# Database_api_username = "Divyachandrpandi"
# paassowrd="passhatj"
TMDB_ENDPOINT = "https://api.themoviedb.org/3/search/movie"

TMDB_APIKEY = "e2445d55fc35f6abb011fc7f95372cb7"

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moviesnew.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Movie(db.Model):
    id = db.Column('books_id', db.Integer, primary_key=True)
    title = db.Column(db.String(200), unique=True, nullable=True)
    year = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(2000), nullable=True)
    rating = db.Column(db.Float, nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(200), nullable=True)
    img_url = db.Column(db.String(2000), nullable=True)


# db.create_all()
# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's
#     sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads
#     to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
#
# db.session.commit()


@app.route("/")
def home():
    all_movies = Movie.query.order_by(Movie.rating).all()

    # This line loops through all the movies
    for i in range(len(all_movies)):
        # This line gives each movie a new ranking reversed from their order in all_movies
        all_movies[i].ranking = len(all_movies) - i
    db.session.commit()
    return render_template("index.html", movies=all_movies)


@app.route("/add", methods=["POST", "GET"])
def add():
    add_movie_form = AddMovie()
    if add_movie_form.validate_on_submit():
        movie_to_search = add_movie_form.title.data
        query = {
            "api_key": TMDB_APIKEY,
            "language": "en-US",
            "query": movie_to_search
        }
        response = requests.get(TMDB_ENDPOINT, params=query).json()
        data = response["results"]  # gives list of dictionary
        return render_template("select.html", options=data)

    return render_template('add.html', form=add_movie_form)


@app.route("/select/<int:id>", methods=["POST", "GET"])
def api_to_db(id):
    query = {
        "api_key": TMDB_APIKEY,
    }
    response = requests.get(url=f"https://api.themoviedb.org/3/movie/{id}", params=query).json()
    print(response)
    title = response['original_title']
    img_url = response['poster_path']
    year = response['release_date'].split("-")[0]
    description = response['overview']
    new_movie = Movie(
        title=title,
        year=year,
        description=description,
        img_url=f"https://image.tmdb.org/t/p/w500{img_url}")
    db.session.add(new_movie)
    db.session.commit()
    print(new_movie.id)

    return redirect(url_for('update', id=new_movie.id))


@app.route('/update/<int:id>', methods=["POST", "GET"])
def update(id):
    movie_form = MovieForm()
    # movie_id = request.args.get("id")
    movie_selected = Movie.query.get(id)

    if movie_form.validate_on_submit():
        movie_selected.review = movie_form.review.data
        movie_selected.rating = movie_form.rating.data
        db.session.commit()
        return redirect(url_for('home'))
    print(movie_form.validate_on_submit())
    print(movie_form.errors)
    print(movie_selected.title)
    return render_template('edit.html', form=movie_form, n_movie=movie_selected)


@app.route('/delete/<int:id>')
def delete(id):
    movie_to_delete = Movie.query.get(id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
