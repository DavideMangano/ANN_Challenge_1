import os
import shutil
import secrets

INPUT_PATH = "./VillagePlantHealty/"
OUTPUT_PATH = "./balanced_dataset_healty/training/"
NUM_OF_PICS = 1200

dirs = list(os.listdir(INPUT_PATH))

sum = 0

for dir in dirs:
    pics = list(os.listdir(INPUT_PATH + dir))
    pics_count = 0

    # creates label directory if it doesn't exists already
    if not os.path.exists(OUTPUT_PATH + dir):
         os.mkdir(OUTPUT_PATH + dir)
    
    # copies random pictures from original dataset until we get to the predifined number
    while pics_count < NUM_OF_PICS and len(pics) > 0:

        # pics a random image to copy
        current_pic = secrets.choice(pics)

        shutil.copy(
            INPUT_PATH + dir + "/" + current_pic, 
            OUTPUT_PATH + dir + "/" + current_pic)

        # removes image from the list
        pics.remove(current_pic)

        pics_count = pics_count + 1
    
    print(dir + " : "  + str(pics_count) + " pictures")
