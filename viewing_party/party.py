from viewing_party.constants import (
    KEY_MOVIE_GENRE,
    KEY_MOVIE_HOST,
    KEY_MOVIE_RATING,
    KEY_MOVIE_TITLE,
    KEY_USER_FAVORITES,
    KEY_USER_FRIENDS,
    KEY_USER_SUBSCRIPTIONS,
    KEY_USER_WATCHED,
    KEY_USER_WATCHLIST,
)


# ------------- WAVE 1 --------------------
def create_movie(title, genre, rating):
    if not title or not genre or not rating:
        return None

    movie = {
        KEY_MOVIE_TITLE: title,
        KEY_MOVIE_GENRE: genre,
        KEY_MOVIE_RATING: rating,
    }
    return movie


def add_to_watched(user_data, movie):
    user_data[KEY_USER_WATCHED].append(movie)
    return user_data


def add_to_watchlist(user_data, movie):
    user_data[KEY_USER_WATCHLIST].append(movie)
    return user_data


def watch_movie(user_data, title):
    movie = get_movie_in_list(user_data[KEY_USER_WATCHLIST], title)

    if movie:
        user_data[KEY_USER_WATCHLIST].remove(movie)
        user_data[KEY_USER_WATCHED].append(movie)

    return user_data


# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------
def get_watched_avg_rating(user_data):
    total_rating = 0.0

    if not user_data[KEY_USER_WATCHED]:
        return 0.0

    for movie in user_data[KEY_USER_WATCHED]:
        total_rating += movie[KEY_MOVIE_RATING]

    avg = total_rating / len(user_data[KEY_USER_WATCHED])
    return avg


def get_most_watched_genre(user_data):
    most_watched = None

    if not user_data[KEY_USER_WATCHED]:
        return None

    genres = {}

    for movie in user_data[KEY_USER_WATCHED]:
        genres[movie[KEY_MOVIE_GENRE]] = genres.get(movie[KEY_MOVIE_GENRE], 0) + 1

    most_watched = max_genres(genres)

    return most_watched

# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------
def get_unique_watched(user_data):
    friends_watched_titles = set()

    for friend in user_data[KEY_USER_FRIENDS]:
        for friend_watched in friend[KEY_USER_WATCHED]:
            friends_watched_titles.add(friend_watched[KEY_MOVIE_TITLE])

    unique_movies_list = []

    for movie in user_data[KEY_USER_WATCHED]:
        if movie[KEY_MOVIE_TITLE] not in friends_watched_titles:
            unique_movies_list.append(movie)

    return unique_movies_list


def get_friends_unique_watched(user_data):
    user_watched_titles = set()

    for movie in user_data[KEY_USER_WATCHED]:
        user_watched_titles.add(movie[KEY_MOVIE_TITLE])

    unique_movies_list = []
    friend_watched_titles = set()

    for friend in user_data[KEY_USER_FRIENDS]:
        for movie in friend[KEY_USER_WATCHED]:
            if (
            movie[KEY_MOVIE_TITLE] not in user_watched_titles
            and movie[KEY_MOVIE_TITLE] not in friend_watched_titles
            ):
                unique_movies_list.append(movie)
                friend_watched_titles.add(movie[KEY_MOVIE_TITLE])

    return unique_movies_list

# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------
def get_available_recs(user_data):
    available_recs = []
    friends_unique_watched = get_friends_unique_watched(user_data)
    subscribed_hosts = set(user_data[KEY_USER_SUBSCRIPTIONS])

    for movie in friends_unique_watched:
        if movie[KEY_MOVIE_HOST] in subscribed_hosts:
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
        if movie[KEY_MOVIE_GENRE] == most_watched_genre:
            genre_recommendations.append(movie)

    return genre_recommendations



def get_rec_from_favorites(user_data):
    favorites_recommendations = []
    unique_watched = get_unique_watched(user_data)
    favorites = user_data.get(KEY_USER_FAVORITES, [])

    for movie in unique_watched:
        if movie in favorites:
            favorites_recommendations.append(movie)

    return favorites_recommendations


# =================== helper functions =====================
def get_movie_in_list(user_list,title):
    if title is None or user_list is None:
        return None

    for movie in user_list:
        if movie[KEY_MOVIE_TITLE].lower() == title.lower():
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
