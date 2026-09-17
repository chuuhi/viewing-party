# ------------- WAVE 1 --------------------


def create_movie(title, genre, rating):

    if title is None or genre is None or rating is None:
        return None

    movie = {
        "title" : title,
        "genre" : genre ,
        "rating" : rating 
    }
    return movie

def add_to_watched(user_data, movie):

    if user_data.get("watched") is None:
        user_data["watched"]=[]

    if movie not in user_data["watched"]:
        user_data["watched"].append(movie)

    return user_data


def add_to_watchlist(user_data, movie):

    if user_data.get("watchlist") is None:
        user_data["watchlist"]=[]

    if movie not in user_data["watchlist"]:
        user_data["watchlist"].append(movie)

    return user_data


def watch_movie(user_data, title):
    if user_data is None or title is None:
        return None

    movie = get_movie_in_list(user_data["watchlist"],title)
    if movie:
        user_data["watchlist"].remove(movie)

        if not user_data["watched"]:
            user_data["watched"] = []

        user_data["watched"].append(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0.0

    if user_data.get("watched") is None or len(user_data["watched"]) == 0:
        return 0.0

    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    avg = total_rating/len(user_data["watched"])
    return avg


def get_most_watched_genre(user_data):
    most_watched = None

    if user_data.get("watched") is None or len(user_data["watched"]) == 0:
        return None

    genres = {}

    for movie in user_data["watched"]:
        genres[movie["genre"]] = genres.get(movie["genre"], 0) + 1

    most_watched = max_genres(genres)

    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    unique_movies_list = []

    for movie in user_data["watched"]:
        is_movie_unique = True
        for friend in user_data["friends"]:
            for friend_watched in friend["watched"]:
                if movie["title"] == friend_watched["title"]:
                    is_movie_unique = False
        if is_movie_unique:
            unique_movies_list.append(movie)
    return unique_movies_list

def get_friends_unique_watched(user_data):
    unique_movies_list = []

    for friend in user_data["friends"]:
        for movie in friend["watched"]:
            is_movie_unique = True

            for user_movie in user_data["watched"]:
                if movie["title"] == user_movie["title"]:
                    is_movie_unique = False
            if is_movie_unique:
                if movie not in unique_movies_list:
                    unique_movies_list.append(movie)
    return unique_movies_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    available_recs = []
    friends_unique_watched = get_friends_unique_watched(user_data)

    for movie in friends_unique_watched:
        if movie["host"] in user_data["subscriptions"]:
            available_recs.append(movie)

    return available_recs


# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------

def get_new_rec_by_genre(user_data):
    genre_recommendations = []
    most_watched_genre = get_most_watched_genre(user_data)
    friends_unique_watched = get_friends_unique_watched(user_data)

    if most_watched_genre is None:
        return genre_recommendations

    for movie in friends_unique_watched:
        if movie["genre"] == most_watched_genre:
            genre_recommendations.append(movie)

    return genre_recommendations



def get_rec_from_favorites(user_data):
    favorites_recommendations = []
    unique_watched = get_unique_watched(user_data)
    favorites = user_data.get("favorites", [])

    for movie in unique_watched:
        if movie in favorites:
            favorites_recommendations.append(movie)

    return favorites_recommendations


# =================== helper functions =====================
def get_movie_in_list(user_list,title):
    if title is None or user_list is None:
        return None

    for movie in user_list:
        if movie["title"].lower() == title.lower():
            return movie
    return None

def max_genres(genres):
    max_genre = None
    max_count = 0

    for genre, count in genres.items():
        if count > max_count:
            max_count = count
            max_genre = genre

    return max_genre
# ================================================================