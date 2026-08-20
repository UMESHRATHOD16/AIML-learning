def list_all_videos(videos):
    pass

def add_video(videos):
    pass

def update_video(videos):
    pass

def delete_video(videos):
    pass


videos = []


while True:
    print("---- YOUTUBE MANAGER ----")
    print("---------------------------")
    print("Choose an option ")
    print("1. List all youTube videos ")
    print("2. Add a youTube video ")
    print("3. Update a youTube video details ")
    print("4. Delete a youTube video ")
    print("5. Exit ")
    choice = input("Enter Your Choice: ")

    match choice:
        case '1':
            list_all_videos(videos)
        case '2':
            add_video(videos)
        case '3':
            update_video(videos)
        case '4':
            delete_video(videos)
        case '5':
            print("See You Next Time !!\n")
            break
        case _:
            print(" Invalid Input !! ")
            break


