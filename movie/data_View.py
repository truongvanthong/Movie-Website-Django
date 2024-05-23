import os
from django.core.wsgi import get_wsgi_application 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'movie.settings') 
application = get_wsgi_application() 

import random
from faker import Faker
from datetime import datetime
from myapp.models import ViewerMovie, Viewer, Movie

fake = Faker('en_US')
Faker.seed(0)  # Đặt seed cho các giá trị ngẫu nhiên

def create_fake_viewers(num_viewers):
    for _ in range(num_viewers):
        username = fake.user_name()
        email = fake.email()
        password = fake.password()
        dob = fake.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=100)

        # Kiểm tra xem username đã tồn tại hay chưa
        existing_viewer = Viewer.objects.filter(username=username)

        if not existing_viewer.exists():
            viewer = Viewer(username=username, email=email, dob=dob)
            viewer.set_password(password)
            viewer.save()

def create_fake_viewer_movie(num_records):
    for _ in range(num_records):
        viewer_id = random.choice(Viewer.objects.all()).pk
        movie_id = random.choice(Movie.objects.all()).pk
        watched = random.randint(1, 100)
        favourite = random.choice([0, 1])
        rating = random.randint(1, 10)
        review = fake.sentence()
        rtime = fake.date_between(start_date='-2y', end_date='now')

        # Kiểm tra xem bản ghi tương tự đã tồn tại chưa
        existing_record = ViewerMovie.objects.filter(
            viewer_id=viewer_id,
            movie_id=movie_id
        )

        if not existing_record.exists():
            viewer_movie = ViewerMovie(
                viewer_id=viewer_id,
                movie_id=movie_id,
                watched=watched,
                favourite=favourite,
                rating=rating,
                review=review,
                rtime=rtime
            )
            viewer_movie.save()


# # Tạo người xem giả
# print("Creating fake viewers...")
# create_fake_viewers(5)
# print("Done creating fake viewers")
# # Tạo bản ghi giả cho ViewerMovie
# print("Creating fake viewer movie...")
# create_fake_viewer_movie(10)
# print("Done creating fake viewer movie")

# Tạo vòng for hiện tqdm chạy Tạo nguoi xem giả
from tqdm import tqdm
for _ in tqdm(range(10)):
    # tạo người xem giả
    create_fake_viewers(10)
    # tạo bản ghi giả cho ViewerMovie
    create_fake_viewer_movie(500)
    