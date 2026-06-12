from flask import Flask, render_template, send_from_directory
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)

@app.route("/")
def home():

    music_folder = os.path.join(BASE_DIR, "music")

    playlists = {}

    if os.path.exists(music_folder):

        for folder in os.listdir(music_folder):

            folder_path = os.path.join(music_folder, folder)

            if os.path.isdir(folder_path):

                songs = []

                for file in os.listdir(folder_path):

                    if file.lower().endswith(".mp3"):

                        songs.append({
                            "filename": file,
                            "title": os.path.splitext(file)[0]
                        })

                playlists[folder] = songs

    return render_template(
        "index.html",
        playlists=playlists
    )

@app.route("/music/<path:filename>")
def music(filename):

    return send_from_directory(
        os.path.join(BASE_DIR, "music"),
        filename
    )

if __name__ == "__main__":
    app.run(debug=True)