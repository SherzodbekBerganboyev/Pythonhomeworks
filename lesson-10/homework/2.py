import requests
import random

# TMDB API kalit
API_KEY = "fb916e262cc3d4c7a32ff3ee8d4de642"
BASE_URL = "https://api.themoviedb.org/3"

# Janrlar ro'yxatini olish
def get_genres():
    url = f"{BASE_URL}/genre/movie/list?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    genres = data.get("genres", [])
    return {genre["name"].lower(): genre["id"] for genre in genres}

# Janrga mos kinolarni olish
def get_movies_by_genre(genre_id):
    url = f"{BASE_URL}/discover/movie?api_key={API_KEY}&with_genres={genre_id}&sort_by=popularity.desc"
    response = requests.get(url)
    data = response.json()
    return data.get("results", [])

# Tavsiya funksiyasi
def recommend_movie():
    genre_map = get_genres()
    print("\n🎭 Mavjud janrlar:")
    for genre in genre_map:
        print(f" - {genre.title()}")

    # Foydalanuvchidan janr nomini olish
    genre_name = input("\nQaysi janrdagi filmni istaysiz? ").lower()

    if genre_name in genre_map:
        genre_id = genre_map[genre_name]
        movies = get_movies_by_genre(genre_id)
        if movies:
            movie = random.choice(movies)
            print("\n🎬 Tavsiya etilgan film:")
            print(f"Nomi: {movie.get('title', 'Nomaʼlum')}")
            print(f"Tavsifi: {movie.get('overview', 'Tavsif mavjud emas.')}")
            print(f"Reyting: {movie.get('vote_average', 'Nomaʼlum')}")
        else:
            print("❗ Ushbu janrda film topilmadi.")
    else:
        print("❗ Bunday janr topilmadi. To'g'ri nom kiriting.")

# Dasturni ishga tushirish
recommend_movie()
