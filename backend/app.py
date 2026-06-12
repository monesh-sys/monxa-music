from flask import Flask, render_template, send_from_directory
import os

# Get project root folder (IMPORTANT for correct paths)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)

# ----------------------------
# HOME PAGE (Load playlists)
# ----------------------------
@app.route("/")
def home():

    music_folder = os.path.join(BASE_DIR, "music")
    playlists = {}

    # Check if music folder exists
    if os.path.exists(music_folder):

        # Loop through playlist folders
        for folder in sorted(os.listdir(music_folder)):

            folder_path = os.path.join(music_folder, folder)

            if os.path.isdir(folder_path):

                songs = []

                # Loop through mp3 files
                for file in sorted(os.listdir(folder_path)):

                    if file.lower().endswith(".mp3"):

                        songs.append({
                            "filename": file,
                            "title": os.path.splitext(file)[0]
                        })

                playlists[folder] = songs

    return render_template("index.html", playlists=playlists)


# ----------------------------
# MUSIC FILE ROUTE
# ----------------------------
@app.route("/music/<filename>")
def music(filename):
    return send_from_directory(
        os.path.join(BASE_DIR, "music"),
        filename
    )/89+6

# ----------------------------
# RUN APP
# ----------------------------
if __name__ == "__main__":
    app.run(debug=True)
