import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_data_helpers(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n")
    print("*" * 70)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("\n")
    print("*" * 70)


def add_video(videos):
    name = input('Enter video name:')
    time = input('Enter video time:')
    videos.append({"name":name, "time":time})
    save_data_helpers(videos)


def update_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to update '))
    if 0 <= index <= len(videos): 
        name = input('Enter the video name ')
        time = input('Enter the video time ')
        videos[index-1] = {'name': name, 'time': time }
        save_data_helpers(videos)
    else:
        print("Invalid video number.")


def delete_video(videos):
    list_all_videos(videos)
    index = int(input('Enter the video number to delete '))
    if 0<=index <= len(videos):
        del videos[index-1]
        save_data_helpers(videos)
        print("Video deleted successfully.")
    else:
        print("Invalid video number.")



def main():
    videos = load_data()
    while True:
        print("\n Youtube Manager | choose an option ")
        print("1. List all videos ")
        print("2. add youtube video ")
        print("3. update a youtube video ")
        print("4. delete youtube video ")
        print("5. exit the app ")

        choice = input("Enter your choice ")

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
                break
            case _:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


