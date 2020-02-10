import os

test_folder = "./test"
train_folder = "/T-friend_data/TRAIN/prod/"
train_res_folder = "/T-friend_data/TRAIN/res/"#don't used
req_folder = "/T-friend_data/REQ/prod/"
res_folder = "/T-friend_data/RES/prod/"

folder_list = [test_folder, train_folder, train_res_folder, req_folder, res_folder]

for folder in folder_list:
    if not os.path.exists(folder):
        os.mkdir(folder)
