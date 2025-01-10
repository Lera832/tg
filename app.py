from flask import Flask, jsonify

app = Flask(__name__)

MOVIES = [
    {"id": 1, "title": "Фильм 1", "file_url": "https://example.com/movie1.mp4"},
    {"id": 2, "title": "Фильм 2", "file_url": "https://example.com/movie2.mp4"},
]

@app.route('/movies')
def get_movies():
    """Возвращает список фильмов."""
    return jsonify(MOVIES)

if __name__ == "__main__":
    app.run(debug=True)
