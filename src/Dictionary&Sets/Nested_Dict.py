movie = {
    "bolly" : "joker",
    "holly" : {
        "a" : "iron man",
        "b" : "thor",
        "c" : "spiderman"
    }
}

print(movie)
print(movie.keys())
print(len(movie))
print(movie.keys()) #return all keys
print(movie.values())  #return all values
print(movie.items())  #return all key value pair as tuples
print(movie.get("holly"))
print(movie.get("bolly"))