const audio = document.getElementById("audio");
const title = document.getElementById("title");

function playSong(song,name)
{
    audio.src = song;
    audio.play();
    title.innerHTML = name;
}