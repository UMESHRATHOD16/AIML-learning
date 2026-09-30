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

def list_videos():
    cursor.execute("SELECT * FROM videos")
    for row in cursor.fetchall():
        print(row)

def add_video(name,time):
    cursor.execute("INSERT INTO videos (name, time) VALUES (?, ?)", (name, time))
    conn.commit()

def update_video(video_id,new_name,new_time):
    cursor.execute("UPDATE videos SET name = ?, time = ? WHERE id = ?", (new_name, new_time, video_id))
    conn.commit()

def delete_video(video_id):
    cursor.execute("DELETE FROM videos where id = ?", (video_id,))
    conn.commit()


def main():
    while True :
        print("Youtube Manager App With sqlite3")
        print('1. List Videos')
        print('2. Add Videos')
        print('3. Update Video')
        print('4. Delete Videos')
        print('5. Exit App')

        choice = input("Enter your choice: ")

        if choice == "1" :
            list_videos()
        
        elif choice == "2" :
            name = input("Enter video name: ")
            time = input("Enter video time/duration: ")
            add_video(name,time)

        elif choice == "3" :
            video_id = input("Enter video id to update: ")
            new_name = input("Enter new video name: ")
            new_time = input("Enter new video time/duration: ")
            update_video(video_id,new_name,new_time)
        
        elif choice == "4" :
            video_id = input("Enter video id to delete: ")
            delete_video(video_id)

        elif choice == "5" :
            print("Exiting......")
            break
        else:
            print("Invalid Choice!")
    conn.close()



if __name__ == "__main__" :
    main()