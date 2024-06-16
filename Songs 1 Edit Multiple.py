# Add image in songs also album and artist names
import os
import eyed3

# Specify the folder containing your MP3 files with double backslashes or a raw string
mp3_folder = r"C:\\Users\\RanaUniverse\\Desktop\\1895194333"

# Specify the path to the image file you want to use as album art with double backslashes or a raw string
album_art_file = r"C:\\Users\\RanaUniverse\\Desktop\\RU 9b UPI QR Code.png"

# Iterate through the MP3 files in the folder
for filename in os.listdir(mp3_folder):
    if filename.endswith(".mp3"):
        mp3_path = os.path.join(mp3_folder, filename)
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
        print(f"Changed metadata for {filename}")

print("Metadata and album art changed for all MP3 files.")
