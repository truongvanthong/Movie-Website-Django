import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "movie.settings") # Tên app bạn tạo ( QUAN TRỌNG ).
django.setup()
from myapp.models import Movie # Import Model đã tạo 

class DataObject():

    def __init__(self):
        pass

    def create(self, title, year, genre, plot, lang ,poster, rating, trailor, runtime, budget, revenue, director, director_img, top_cast, top_cast_img):
        # Ta sẽ insert data bằng phương thức create
        return Movie.objects.create(title=title, year=year, genre=genre, plot=plot, lang=lang ,poster=poster, rating=rating, trailor=trailor, runtime=runtime, budget=budget, revenue=revenue, director=director, director_img=director_img, top_cast=top_cast, top_cast_img=top_cast_img)
