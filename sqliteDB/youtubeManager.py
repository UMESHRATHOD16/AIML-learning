import sqlite3

conn = sqlite3.connect('youtube_videos.db')
cursor = conn.cursor()

cursor.execute(''' 
    CREATE TABLE IF NOT EXISTS videos (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                time TEXT NOT NULL
    
    )
''')

def main():
    while True :
        print("Youtube Manager App With sqlite3")
        print('1. List Videos')
        print('2. Add Videos')
        print('3. Update Video')
        print('4. Delete Videos')
        print('5. Exit App')


if __name__ == "__main__" :
    main()