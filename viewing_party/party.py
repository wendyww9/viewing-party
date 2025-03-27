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

def watch_movie(user_data, title):
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
    """
    Calculates the average rating of watched movies.

    Returns:
    float: The average rating of watched movies, or 0.0 if none are watched.
    """

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
    """
    Determines the most watched genre among watched movies.

    Returns:
    str: The most watched genre, or None if no movies have been watched.
    """

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
    """
    Finds movies that the user has watched but their friends haven't.

    Returns:
    list: A list of movies watched only by the user.
    """

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
    """
    Finds movies that friends have watched but the user hasn't.

    Returns:
    list: A list of movies watched only by friends.
    """

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
    """
    Recommends movies that friends have watched but the user hasn't, 
    and are available on the user's subscribed services.

    Returns:
    list: A list of recommended movies.
    """

    friends_unique_watched = get_friends_unique_watched(user_data)
    user_subscriptions = user_data.get("subscriptions", [])

    recommendations = [movie for movie in friends_unique_watched if movie["host"] in user_subscriptions]

    return recommendations

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    """
    Recommends movies from friends' unique watched list that match the user's most watched genre.

    Returns:
    list: A list of recommended movies in the most watched genre.
    """
        
    friends_unique_watched = get_friends_unique_watched(user_data)
    common_genre = get_most_watched_genre(user_data)

    recommendations = [movie for movie in friends_unique_watched if movie["genre"] == common_genre]

    return recommendations

def get_rec_from_favorites(user_data):
    """
    Recommends movies that are in the user's favorites list and are unique to the user.

    Returns:
    list: A list of recommended movies from favorites.
    """

    favorites = user_data.get("favorites", [])
    unique_watched = get_unique_watched(user_data)

    recommended_movies = [movie for movie in unique_watched if movie in favorites]

    return recommended_movies


