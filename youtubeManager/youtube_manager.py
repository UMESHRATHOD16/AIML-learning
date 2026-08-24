import json


database = "Youtube.txt"

def load_data():
    try:
        with open(database,'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []


def list_all_videos(videos):
    print("\n")
    print("*"*70)
    for index, video in enumerate(videos, start=1):
        print(f'{index}. {video['name']}, Duration : {video['time']}')
    print("\n")
    print("*"*70)

def add_video(videos):
   name =  input("Enter Video Name:")
   time = input("Enter Video Time:")
   videos.append({
       'name':name,
       'time':time,

   })
   save_data_helper(videos)

def update_video(videos):
    pass

def delete_video(videos):
    pass

def save_data_helper(videos):
    with open(database,'w') as file :
        json.dump(videos,file)
        


def main():
    videos = load_data()
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

if __name__ == "__main__":
    main()

