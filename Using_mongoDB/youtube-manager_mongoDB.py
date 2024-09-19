
from pymongo import MongoClient 
from bson import ObjectId


client = MongoClient("mongodb+srv://mauryashekhar13:KoHQnxOQmtUlczke@youtube-manager.yja6i.mongodb.net/")

db = client['youtube-manager']
video_collection = db["videos"]

print(video_collection)


def all_videos():
    for video in video_collection.find():
        print(f"ID: {video['_id']}, Name: {video['name']}, and Time: {video['time']}")

def add_video(name, time):
    video_collection.insert_one({"name": name, "time": time})

def update_video(videoID, new_name, new_time):
    video_collection.update_one(
        {"_id": ObjectId(videoID)},
        { "$set": {"name": new_name, "time": new_time }}
    )


def delete_video(videoID):
    video_collection.delete_one({"_id": ObjectId(videoID)})




def main():
    while True:
        print("\nChoose an option:")
        print("1. List all videos ")
        print("2. Add a new video ")
        print("3. Update a video ")
        print("4. Delete a video ")
        print("5. Exit ")
        choice  = input("Choose an option: ")

        if choice == "1":
            all_videos()
        elif choice == "2":
            name = input("Enter a video name: ")
            time = input("Enter a video duration: ")
            add_video(name, time)        
        elif choice == "3":
            videoID = input("Enter a video ID: ")
            name = input("Enter a video name: ")
            time = input("Enter a video duration: ")
            update_video(videoID, name, time)
        elif choice == "4":
            videoID = input("Enter a video ID: ")
            delete_video(videoID)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")




if __name__ == "__main__":
    main()
