# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    movie = {
        "title": title,
        "genre": genre,
        "rating": rating, 
    }
    return movie


def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data


def watch_movie(user_data, title):
    movie = get_movie_in_list(user_data["watchlist"], title)

    if movie:
        user_data["watchlist"].remove(movie)
        user_data["watched"].append(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0.0

    if not user_data["watched"]:
        return 0.0

    for movie in user_data["watched"]:
        total_rating += movie["rating"]

    avg = total_rating / len(user_data["watched"])
    return avg


def get_most_watched_genre(user_data):
    most_watched = None

    if len(user_data["watched"]) == 0:
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
    friends_watched_titles = []
    for friend in user_data.get("friends", []):
        for friend_watched in friend.get("watched", []):
            friends_watched_titles.append(friend_watched["title"])

    unique_movies_list = []
    for movie in user_data.get("watched", []):
        if movie["title"] not in friends_watched_titles:
            unique_movies_list.append(movie)
    return unique_movies_list

def get_friends_unique_watched(user_data):
    user_watched_titles = []
    for movie in user_data.get("watched", []):
        user_watched_titles.append(movie["title"])

    unique_movies_list = []
    for friend in user_data.get("friends", []):
        for movie in friend.get("watched", []):
            if movie["title"] not in user_watched_titles and movie not in unique_movies_list:
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