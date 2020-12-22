import csv
from random import randint
from pearsonCorrelation import pearsonCorrelation

# Dataset TEST
# ui = [["Star Wars", 1], ["Star Trek", 3],["Need for Speed", 4], ["Home Alone", 5], ["Avengers", 2],
#       ["Scream", 2], ["Juicy", 3], ["Shorta", 2], ["Cola", 3], ["Cartoon", 5], ["Club House", 1], ["Project X", 5]]
#
# uj = [["Star Wars", 5], ["Star Trek", 3],["Need for Speed", 4], ["Home Alone", 5], ["Avengers", 2],
#       ["Scream", 2], ["Juicy", 3], ["Shorta", 2], ["example", 5], ["Scooby Doo", 2]]

# Finds the info about the user
def findInfoForPerson(userID):
    list = []

    for x in ratings:
        if (x[0] == userID):
            list.append(x)

    return list

# Find the movie and rating from the user
def findMovieAndRatings(listInfo):
    result = []

    for x in listInfo:
        ratingAndMoviename = [x[2], int(x[3])]
        result.append(ratingAndMoviename)

    return result

# Action | Adventure | Animation |
# #               Children's | Comedy | Crime | Documentary | Drama | Fantasy |
# #               Film-Noir | Horror | Musical | Mystery | Romance | Sci-Fi |
# #               Thriller | War | Western |

# Finds the genre from a movie
def findGenreToMovie(movieNames):

    genre = []
    movieName = []
    moviesGenres = []

    with open("ratingsCSV.csv", "r") as r:
        reader = csv.reader(r)

        for m in reader:
            if(m[2] in movieNames and m[2] not in movieName):
                movieName.append(m[2])
                genre.append(m[4:])

        # combine the movie with the genre
        for m, g in zip(movieName, genre):
            l = [m]
            for gs in g:
                l.append(gs)

            moviesGenres.append(l)

    return moviesGenres

# Determine the sum of the active user
def findSumOfGenre(userID):
    info = findInfoForPerson(userID)

    genreSum = {"Action": 0, "Adventure": 0, "Animation": 0, "Children's": 0, "Comedy": 0
            ,"Crime": 0, "Documentary": 0, "Drama": 0,  "Fantasy": 0, "Film-Noir": 0,
            "Horror": 0,  "Musical": 0, "Mystery": 0,
            "Romance": 0, "Sci-Fi": 0, "Thriller": 0,  "War": 0, "Western": 0}

    genreProcent = {"Action": 0, "Adventure": 0, "Animation": 0, "Children's": 0, "Comedy": 0
        , "Crime": 0, "Documentary": 0, "Drama": 0, "Fantasy": 0, "Film-Noir": 0,
                "Horror": 0, "Musical": 0, "Mystery": 0,
                "Romance": 0, "Sci-Fi": 0, "Thriller": 0, "War": 0, "Western": 0}

    sumOfAllGenre = 0

    # [4:21]
    for x in info:
        for e, (k) in enumerate(genreSum.keys(), start=4):
             if(int(x[e]) == 1):
                 genreSum[k] += 1
                 sumOfAllGenre += 1

    for e, v in enumerate(genreSum.keys()):
        genreProcent[v] = round(genreSum[v] / sumOfAllGenre * 100)

    return genreProcent

# Find which movies that should be recommendede
def findRecommendation(dictProcent, moviesList):

    moviesToRecommendInfo = []
    moviesToRecommend = []

    genre = []
    movieName = 0
    score = 0

    while(len(moviesToRecommend) < 10):
        for m in range(len(moviesList)):
            sum = 0
            genre = []

            for e, (g) in enumerate(moviesList[m][1:]):

                score = g
                movieName = moviesList[m][0]

                if (score == str(0)):
                    continue

                if(movieName in moviesToRecommend):
                    continue

                gen = list(dictProcent.keys())[e]
                genreProcent = dictProcent[gen]
                movieName = moviesList[m][0]

                genre.append([gen, score, genreProcent])
                sum += genreProcent

            randV = randint(0, 100)

            if(randV <= sum):
                genre.insert(0, movieName)
                moviesToRecommendInfo.append(genre)
                moviesToRecommend.append(movieName)
                break

    for m in moviesToRecommendInfo:
        print(m)

# START
ratings = []
with open("ratingsCSV.csv", "r") as ra:
    reader = csv.reader(ra)

    for r in reader:
        ratings.append(r)

# PICK MAIN USER / active user
userID = str(366)
userInfo_1 = findInfoForPerson(userID)
userRatings_1 = findMovieAndRatings(userInfo_1)

listPearsonValues = []

for x in range(943):
    x += 1
    x = str(x)

    if(x == userID):
        continue

    userInfo_2 = findInfoForPerson(x)
    userRatings_2 = findMovieAndRatings(userInfo_2)

    pearsonObject =  pearsonCorrelation(userRatings_1, userRatings_2)

    list1, list2, diff1 = pearsonObject.findSimilaryItems()

    pearsonObject.findPearsonCorrelation(list1, list2)

    pearsonValue = pearsonObject.returnPearsonCorreation()

    pearsonValuesX = [pearsonValue, x, diff1]

    listPearsonValues.append(pearsonValuesX)

highestValue = 0
userHighest = 0
diff1 = 0

for m in listPearsonValues:
    PValue = m[0]
    PX = m[1]
    diff1 = m[2]

    if(PValue > highestValue):
        highestValue = PValue
        userHighest = PX

# print(highestValue)
# print(userHighest)
# print(len(diff1))

findRecommendation(findSumOfGenre(userID), findGenreToMovie(diff1))











