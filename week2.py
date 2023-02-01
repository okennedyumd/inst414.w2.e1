import json
with open("imdb_movies_1985to2022.json", "r") as file:
    hugh_movies = []
    avg_score = 0
    for line in file:
        movie = json.loads(line)
        actors = movie["actors"]
        for actor in actors:
            actor_name = actor[1]
            if actor_name == "Hugh Jackman":
                hugh_movies.append(movie)
    for movie in hugh_movies:
        print(movie['rating'])
        
    