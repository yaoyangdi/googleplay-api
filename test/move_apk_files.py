import os
import shutil

# Path to the folder containing the apk file
folder_path = r"E:\apk_dataset"

# List of all subfolders in a folder
subfolders = [subfolder for subfolder in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, subfolder))]

# List of all apk files
apk_files = [file for file in os.listdir(folder_path) if file.endswith(".apk")]

# Iterate through all apk files
for apk_file in apk_files:
    # Extract the prefix of apk file name
    prefix = apk_file.split('_')[0]

    # Iterate through all subfolders
    for subfolder in subfolders:
        # Prefix of the apk file is the same as the name of the subfolder & there is no file with the same name in the subfolder
        if prefix == subfolder and apk_file not in os.listdir(os.path.join(folder_path, subfolder)):
            # Move the apk file to the corresponding subfolder
            shutil.move(os.path.join(folder_path, apk_file), os.path.join(folder_path, subfolder, apk_file))
            break

print("Done!")


# # Create an empty dictionary to store the apk list corresponding to each prefix
# prefix_dict = {}
#
#
# # Iterate through all apk files
# for apk in apk_files:
#     # Extract the prefix of apk file name
#     prefix = os.path.basename(apk).split('_')[0]
#     if prefix in prefix_dict:
#         prefix_dict[prefix].append(apk)
#     # If the prefix not in the dictionary, create a new key-value pair
#     else:
#         prefix_dict[prefix] = [apk]
#
# # Iterate prefix dictionary
# for prefix, apks in prefix_dict.items():
#     # Create a folder named with the prefix(package doc id)
#     folder_name = os.path.join(folder_path, prefix)
#     os.makedirs(folder_name, exist_ok=True)

#     # Move apk with same prefix into folder
#     for apk in apks:
#         shutil.move(os.path.join(folder_path, apk), os.path.join(folder_name, apk))
#
# print("Done!")






