# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if title and genre and rating:
        movie = {
            "title": title,
            "genre": genre,
            "rating": rating
        }
        return movie
    else: 
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
    wacthlist = user_data["watchlist"]

    for movie in wacthlist:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    
    avg_rating = 0.0
    count = 0
    sum = 0
    if not user_data["watched"]:
        return avg_rating
    for movie in user_data["watched"]:
        sum += movie["rating"]
        count += 1

    avg_rating = sum / count
    return avg_rating

def get_most_watched_genre(user_data):
    movie_genre = {}
    count = 0
    genre = ""
    if not user_data["watched"]:
        return None
    for movie in user_data["watched"]:
        movie_genre[movie["genre"]] = movie_genre.get(movie["genre"], 0) + 1
        if count < movie_genre[movie["genre"]]:
            count = movie_genre[movie["genre"]]
            genre = movie["genre"]
    return genre

    
# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    
    user_watched = user_data.get("watched", [])
    friends_watched = []
    user_unique_movies = []

    for friend in user_data.get("friends", []):
        friends_watched.extend(friend.get("watched", []))

    for movie in user_watched:
        if movie not in friends_watched and movie not in user_unique_movies:
            user_unique_movies.append(movie)
    
    return user_unique_movies

def get_friends_unique_watched(user_data):
    user_watched = user_data.get("watched", [])
    friends_watched = []
    friends_unique_movies= []

    for friend in user_data.get("friends", []):
        friends_watched.extend(friend.get("watched", []))
        
    for movie in friends_watched:
        if movie not in friends_unique_movies and movie not in user_watched:
            friends_unique_movies.append(movie)
    
    return friends_unique_movies

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):

    friends_unique_watched = get_friends_unique_watched(user_data)
    user_subscriptions = user_data.get("subscriptions", [])

    recommendations = []

    recommendations = [movie for movie in friends_unique_watched if movie["host"] in user_subscriptions]

    return recommendations
# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

