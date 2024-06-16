# Songs Data edit from different folders all at a times

import os
import eyed3

# List of folder directories to process
folder_directories = [
    r"C:\Users\RanaUniverse\Downloads\01 songs\01 Bengal Songs 001-200 Playlist 1627 Songs",
    r"C:\Users\RanaUniverse\Downloads\01 songs\04 Bengal Songs 601-800 Playlist 1627 Songs",
    r"C:\Users\RanaUniverse\Downloads\01 songs\05 Bengal Songs 801-1000 Playlist 1627 Songs",
    r"C:\Users\RanaUniverse\Downloads\01 songs\08 Bengal Songs 1401-1600 Playlist 1627 Songs",
    r"C:\Users\RanaUniverse\Downloads\01 songs\09 Bengal Songs 1601-1627 Playlist 1627 Songs"
]

# folder_directories = [
#     r"C:\\Users\\RanaUniverse\\Desktop\\Folder1",
#     r"C:\\Users\\RanaUniverse\\Documents\\Folder2",
#     r"D:\\Music\\Folder3",
#     r"E:\\MP3s\\Folder4",
#     r"F:\\Audio\\Folder5"
# ]


# Specify the path to the image file you want to use as album art with double backslashes or a raw string
album_art_file = r"C:\\Users\\RanaUniverse\\Desktop\\RU 9b UPI QR Code.png"

# Iterate through each folder directory
for folder_directory in folder_directories:
    # Check if the folder directory exists
    if os.path.exists(folder_directory):
        # Iterate through the MP3 files in the folder
        for folder_name, subfolders, filenames in os.walk(folder_directory):
            for filename in filenames:
                if filename.endswith(".mp3"):
                    mp3_path = os.path.join(folder_name, filename)
                    audiofile = eyed3.load(mp3_path)

                    # Modify album, artist, album artist, and comment
                    audiofile.tag.album = "Rana Universe"
                    audiofile.tag.artist = "Upi Id: RanaUniverse@upi"
                    audiofile.tag.album_artist = "YouTube: https://www.yotube.com/@RanaUniverse"
                    audiofile.tag.comments.set("Pay & Send & Request Money Online: Upi Payment To RanaUniverse@upi")
                    # Set the album art
                    audiofile.tag.images.set(3, open(album_art_file, 'rb').read(), 'image/jpeg')

                    # Save the changes
                    audiofile.tag.save()
                    print(f"Changed metadata for {filename} in folder '{folder_name}'")

print("Metadata and album art changed for MP3 files in all folders.")
