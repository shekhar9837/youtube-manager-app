
def list_all_videos(videos):
    pass

def add_video():
    pass

def update_video():
    pass

def delete_video():
    pass


def main():
    videos =[]
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


