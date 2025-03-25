# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
<<<<<<< HEAD
    if title and genre and rating:
        movie = {
=======
    if title and genre and rating: 
        movie_dict = {
>>>>>>> 25298e14b8044dd43a0ce853c85792056f6c419d
            "title": title,
            "genre": genre,
            "rating": rating
        }
<<<<<<< HEAD
        return movie
    else: 
        return None

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data

=======
        return movie_dict
    else: 
        return None
>>>>>>> 25298e14b8044dd43a0ce853c85792056f6c419d

def add_to_watched(user_data,movie):
    user_data["watched"].append(movie)
    return user_data

def add_to_watchlist(user_data,movie):
    user_data["watchlist"].append(movie)
    return user_data

def watch_movie(user_data,title):
#     - if title in watchlist
#     - remove movie from watchlist
#     - add movie to watched
#     - return user_data
# - else:
#     - return user_data
    wacthlist = user_data["watchlist"]

    for movie in wacthlist:
        if title == movie["title"]:
            user_data["watchlist"].remove(movie)
            user_data["watched"].append(movie)
    return user_data
# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

