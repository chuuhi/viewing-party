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


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------





# =================== helper functions =====================
def get_movie_in_list(user_list,title):
    if title is None or user_list is None:
        return None

    for movie in user_list:
        if movie["title"].lower() == title.lower():
            return movie
    return None
# ================================================================