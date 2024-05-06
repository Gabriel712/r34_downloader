"""
Gabriel712
"""

import requests
import sqlite3
import os

# Define the path to the video folder and the SQLite database
DATABASE_PATH = 'videos.db'
VIDEO_FOLDER = 'videos'

# Check if the video folder exists, create if it does not
if not os.path.exists(VIDEO_FOLDER):
    os.makedirs(VIDEO_FOLDER)

# Establishes a connection to the SQLite database
def get_db_connection():
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Attempts to insert a video into the database
# Returns False if the video already exists or if an error occurs during insertion
def insert_video(conn, video_data):
    """Attempt to insert video into the database and return True if successful."""
    try:
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO videos (hash, owner, url, tags, title, download)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (video_data['hash'], video_data['owner'], video_data['file_url'], video_data['tags'], video_data['title'], 0))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print("Video already exists in the database.")
        return False
    except Exception as e:
        print(f"Error while inserting data into the database: {e}")
        return False

# Downloads a video and updates its status in the database
def download_and_update_video(conn, hash, url):
    """Download video and update database status."""
    try:
        video_path = os.path.join(VIDEO_FOLDER, hash + '.mp4')
        response = requests.get(url)
        if response.status_code == 200:
            with open(video_path, 'wb') as f:
                f.write(response.content)
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE videos SET download = 1 WHERE hash = ?
            """, (hash,))
            conn.commit()
        else:
            print("Failed to download video.")
    except Exception as e:
        print(f"Error: {e}")

# Main function to process video downloads
def main(search_terms):
    """Main function to handle video download and database updates."""
    url = "https://api.rule34.xxx/index.php?page=dapi&s=post&q=index"
    params = {"tags": search_terms, "json": 1}
    response = requests.get(url, params=params)

    if response.status_code == 200:
        if response.text == "":
            print('0 videos found')
            print(f'Search term : {search_terms}')
        else:
            videos = response.json()  # Convert response to JSON
            conn = get_db_connection()  # Establish database connection

            for video in videos:
                if video['image'].endswith('.mp4'):  # Ensure the file is an MP4
                    video_data = {
                        'hash': video['hash'],
                        'owner': video['owner'],
                        'file_url': video['file_url'],
                        'tags': video['tags'],
                        'title': ' '.join(video['tags'].split()[:4])  # Simplified title from tags
                    }
                    if insert_video(conn, video_data):  # Insert video data into database
                        download_and_update_video(conn, video_data['hash'], video_data['file_url'])
            conn.close()
    else:
        print("Failed to access API.")

# Define search terms and call main function
if __name__ == "__main__":
    search_terms = "video 9:16"
    main(search_terms)
