from flask_wtf import FlaskForm
from wtforms import (FloatField, StringField,SubmitField)
from wtforms.validators import InputRequired, Length


class MovieForm(FlaskForm):
    review = StringField(label='Review', validators=[InputRequired(),
                                                   Length(min=5, max=200)])
    rating = FloatField(label='Your Rating Eg: 8, 7.5', validators=[InputRequired()])
    submit = SubmitField('Submit')


class AddMovie(FlaskForm):
    title = StringField(label="Movie Title", validators=[InputRequired()])
    submit = SubmitField('Add Movie')