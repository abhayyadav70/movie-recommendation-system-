# Movie Recommendation System

# Sample movie database with genres and ratings
movies = {
    'The Shawshank Redemption': {'genre': ['Drama'], 'rating': 9.3},
    'The Godfather': {'genre': ['Crime', 'Drama'], 'rating': 9.2},
    'Inception': {'genre': ['Action', 'Sci-Fi'], 'rating': 8.8},
    'The Dark Knight': {'genre': ['Action', 'Crime', 'Drama'], 'rating': 9.0},
    'Pulp Fiction': {'genre': ['Crime', 'Drama'], 'rating': 8.9}
}

def get_user_preferences():
    print("\nWelcome to Movie Recommender!")
    print("Available genres: Action, Drama, Crime, Sci-Fi")
    preferred_genre = input("Enter your preferred genre: ").title()
    min_rating = float(input("Enter minimum rating (0-10): "))
    return preferred_genre, min_rating

def recommend_movies(preferred_genre, min_rating):
    recommendations = []
    for movie, details in movies.items():
        if preferred_genre in details['genre'] and details['rating'] >= min_rating:
            recommendations.append((movie, details['rating']))
    
    return sorted(recommendations, key=lambda x: x[1], reverse=True)

def main():
    preferred_genre, min_rating = get_user_preferences()
    recommendations = recommend_movies(preferred_genre, min_rating)
    
    print("\nRecommended movies for you:")
    if recommendations:
        for movie, rating in recommendations:
            print(f"{movie} (Rating: {rating})")
    else:
        print("No movies found matching your preferences.")

if __name__ == "__main__":
    main()
