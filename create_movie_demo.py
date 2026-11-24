from sqlmodel import Session

from database import engine
from models import Genre, Movie


def create_movie_with_genre():
    with Session(engine) as session:
        try:
            genre = Genre(name="Action")
            session.add(genre)
            session.flush()

            movie = Movie(
                title="New Action Movie",
                in_theaters=True,
                release_year=2024,
                rating=8.5,
                genre_id=genre.id,
            )
            session.add(movie)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"Error occurred: {e}")


create_movie_with_genre()
