import math


# Determine korrelation value for 2 datasets
class pearsonCorrelation:

    # Constructor
    def __init__(self, user1, user2):
        self.user1 = user1
        self.user2 = user2

    # Determine mean
    def findMean(self, list):
        sum = 0

        for f in list:
            sum += f[1] # Index of rating

        if(len(list) != 0):
            return sum / len(list)
        else:
            return 0

    # Find all similary rated movies
    def findSimilaryItems(self):
        list1_movies = []
        list2_movies = []

        # GETS THE MOVIES AND GENRE
        for m in self.user1:
            list1_movies.append(m[0])

        for p in self.user2:
            list2_movies.append(p[0])

        similary_rated_movies = set(list2_movies) & set(list1_movies) # find Similary movies

        diff_between_user2AndUser1 = set(list2_movies) - set(list1_movies) # Movies that user 2 had seen but not user 1
       # diff_between_user1AndUser2 = set(list1_movies) - set(list2_movies) # Movies that user 1 had seen but not user 2

        list1 = []
        for e, (m) in enumerate(self.user1):
            if m[0] in similary_rated_movies:
                p = [m[0], m[1]]
                list1.append(p)

        list2 = []
        for e, (p) in enumerate(self.user2):
            if p[0] in similary_rated_movies:
                m = [p[0], p[1]]
                list2.append(m)

        return  list1, list2, diff_between_user2AndUser1

    # Determine Covariance
    def findCovariance(self, list1, list2, mean1, mean2):
        sum = 0

        for (m, p) in zip(list1, list2):
            result = (m[1] - mean1) * (p[1] - mean2)
            sum += result

        return sum

    # Determine Variance
    def findVariance(self, list, mean):
        sum = 0

        for m in list:
            result = (m[1] - mean) ** 2
            sum += result

        return sum

    # Determine the Correlation value
    def findPearsonCorrelation(self, list1, list2):
        mean1 = self.findMean(list1)
        mean2 = self.findMean(list2)

        self.covariance = self.findCovariance(list1, list2, mean1, mean2)
        self.varianceX = self.findVariance(list1, mean1)
        self.varianceY = self.findVariance(list2, mean2)

    # returning the Correlation value
    def returnPearsonCorreation(self):
        y = (math.sqrt(self.varianceX * self.varianceY))

        if (y != 0):
            return self.covariance / y
        else:
            return 0
