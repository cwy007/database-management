from sqlmodel import Session

from database import engine
from models import Genre, Movie


def create_movie_with_genre():
    with Session(engine) as session:
        try:
            genre = Genre(name="Horror")
            session.add(genre)
            session.flush()

            movie = Movie(
                title="New Horror Movie",
                in_theaters=50,
                release_year=2008,
                rating=8.5,
                genre_id=genre.id,
            )
            session.add(movie)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Rollback occurred: {e}")


create_movie_with_genre()
