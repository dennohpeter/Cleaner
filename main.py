import os
import shutil

"""
    Automatically Organizes files by moving them into their appropriate DIRECTORY
    Examples
    Moving all .mp4,webpm, .mkv into Either Videos Or Music Directory
    Created by: twitter/github@dennohpeter, Computer Technology Student, Maseno University
"""

EXT_IMAGES = ['.png', '.jpg', '.jpeg', '.bmp', '.svg']
EXT_VIDEOS = ['.mp4', '.mkv', '.webm', '.mpeg', '.flv', '.m4a', '.f4v', '.f4a', '.m4b', '.m4r', '.f4b', '.mov', '.avi', '.wmv']
EXT_AUDIOS = ['.mp3', '.wav', '.raw', '.wma']
EXT_DOCS = ['.txt', '.pdf', '.doc', '.docx', '.odt', '.html']
EXT_ISOs = ['.iso']
EXT_ZIPPED = ['.zip', '.tar', '.rar']
EXT_PROGRAMS = ['.deb', '.exe']
EXT_APKS = ['.apk']
# Getting Current Dir and print it
current_dir = os.getcwd()
print("Current Directory is: {}".format(current_dir))
# list all entries in the current Dir
files = os.listdir(".")
# cd to home dir
home = os.path.expanduser("~")
print("Home: {}".format(home))

# Check If Default Category Directories Exist
# Create them if they don't
DIRS = ["Documents", "Music/Audio", 
        "Pictures", "Videos", "Music", "Downloads/ISOs", 
        "Downloads/Zipped", "Downloads/Programs", "Downloads/Apks"]


def create_dir(dir):
    path = "{}/{}".format(home, dir)
    if os.path.exists(path):
        # print("Dir %s already exists not creating it!" % dir)
        pass
    else:
        os.makedirs(path)
        print("Created: %s" % path)

for dir in DIRS:
    # Checks if folder and creates it if not.
    create_dir(dir)
print("Directories Check Completed!!!")


def move(file, dest):
    destination = '{home}/{dest}'.format(home=home, dest=dest)
    if current_dir != destination:
        try:
            shutil.move(file, destination)
        except shutil.Error as error:
            print("%s, so not moved!!!" % error)
    else:
        print("Already in the right directory, not moved.")

count = 0
for file in files:
    filename, extension = os.path.splitext(file)
    if extension in EXT_IMAGES:
        print("Images: {}{}".format(filename, extension))
        move(file,"Pictures")
        count += 1
    elif extension in EXT_VIDEOS:
        # st_size output is in bytes
        file_size_in_mbs = os.stat(file).st_size /1000000
        if file_size_in_mbs > 250:
            # it can be either a movie or mix
            print("---determining if the video is a movie or song---")
            filename = filename.lower()
            if "mix" in filename or "ft" in filename or "song" in filename or "music" in filename or 'dj' in filename or 'feat' in filename or 'official video' in filename:
                # its a song mix, so moving it music dir
                print("------It's a Song: %s moved to Music------" % filename)
                move(file, "Music")
            else:
                # its a movie, moving it to Videos dir
                print("------It's a Movie: %s moved to Videos------" % file)
                move(file, "Videos")
        else:
            # its a song when < 250
            print("It's a Song: %s" % file)
            move(file, "Music")
        count += 1
    elif extension in EXT_AUDIOS:
        print("Audios: {}{}".format(filename, extension))
        move(file, "Music/Audio")
        count += 1
    elif extension in EXT_DOCS:
        print("Documents: {}{}".format(filename, extension)) 
        move(file, "Documents")
        count += 1
    elif extension in EXT_ISOs:
        print("ISOs: {}{}".format(filename, extension)) 
        move(file, "Downloads/ISOs")
        count += 1
    elif extension in EXT_ZIPPED:
        print("Zipped: {}{}".format(filename, extension))
        move(file, "Downloads/Zipped")
        count += 1
    elif extension in EXT_PROGRAMS:
        print("Programs: {}{}".format(filename, extension))
        move(file, "Downloads/Programs")
        count += 1
    elif extension in EXT_APKS:
        print("APKS: {}{}".format(filename, extension))
        move(file, "Downloads/Apks")
        count += 1
    else:
        print("Other File: {}{}".format(filename, extension))
print("Successfully Organized {} Files.".format(count))

    


