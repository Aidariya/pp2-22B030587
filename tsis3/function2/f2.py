#1
def single_score(movie):
    for m in movies:
        if m["name"] == movie and m["imdb"] > 5.5:
            imdb_score = True 
    return imdb_score

#2
def higher_score(movie_name):
    return ['True' for movie in movies if movie["name"] == movie_name and movie["imdb"] > 5.5] 

def movies_above(movies):
    movies_above = []
    for m in movies:
        if m["imdb"] > 5.5:
            movies_above.append(m["name"])
    return movies_above

movies_above(movies)

def sublist_of_movies(movies): 
    movies_greater = [movie["name"] for movie in movies if movie["imdb"] > 5.5] 
    return movies_greater

#3
def category(n):
    category = []
    for m in movies:
        if m["category"] == n:
            category.append(m["name"])
    return category
drama_movies = category("Drama")
print(drama_movies)

#4
def average_score(movies_list):
    movies_scores = []
    for movie in movies_list:
        score = movie["imdb"]
        movies_scores.append(score)
    average_score = sum(movies_scores) / len(movies_scores)
    return average_score
total_average = average_score(movies)
print(average)

#5
def average_to_category(movies,cat_name): 
    cat_movies=return_movie_category(movies,cat_name)
    avg_score=avg_imdb_score(cat_movies)
    return avg_score

print('Average IMDB of movies in the Adventure category is: ')
s2=average_to_category(movies,'Adventure')
print(s2)