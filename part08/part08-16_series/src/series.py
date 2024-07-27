# Write your solution here:

class Series():
    def __init__(self, title, seasons, genres):
        self.title = title
        self.seasons = seasons
        self.genres = genres
        self.rating_sum = 0
        self.rating_amount = 0
        self.average_rate = 0

    def __str__(self):
        rate = "no ratings"
        if self.rating_amount > 0:
            rate = f"{self.rating_amount} ratings, average {self.average_rate} points"
        
        result = (
            f"{self.title} ({self.seasons} seasons)\n"
            f"genres: {', '.join(self.genres)}\n"
            f"{rate}"
        )
        return result

    def rate(self, rating):
        if not (0 <= rating <= 5):
            raise ValueError("Rating has to be 0-5")
        self.rating_amount += 1
        self.rating_sum += rating
        self.average_rate = round(self.rating_sum/self.rating_amount,1)

    def get_average_rate(self):
        return self.average_rate


def minimum_grade(rating: float, series_list: list):
    grade_result = []
    for i in series_list:
        if i.get_average_rate() > rating:
            grade_result.append(i)
    return grade_result

def includes_genre(genre: str, series_list: list):
    genre_result = []
    for i in series_list:
        if genre in i.genres:
            genre_result.append(i)
    return genre_result


if __name__ == "__main__":
    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(6)

    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)

    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)

    series_list = [s1, s2, s3]

    print("a minimum grade of 4.5:")
    for series in minimum_grade(4.5, series_list):
        print(series.title)

    print("genre Comedy:")
    for series in includes_genre("Comedy", series_list):
        print(series.title)