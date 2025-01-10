async function fetchMovies() {
    const response = await fetch("https://your-backend-url/movies"); // URL backend
    const movies = await response.json();
    const container = document.getElementById("movies");
    container.innerHTML = movies
        .map(
            (movie) => `
            <div class="movie">
                <h3>${movie.title}</h3>
                <button onclick="selectMovie('${movie.file_url}')">Смотреть</button>
            </div>
        `
        )
        .join("");
}

function selectMovie(fileUrl) {
    Telegram.WebApp.sendData(JSON.stringify({ file_url: fileUrl })); // Отправить в бот
}

window.onload = fetchMovies;
