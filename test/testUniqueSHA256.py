import os
import hashlib
import shutil
import pandas as pd


def calculate_sha256(file_path):
    sha256 = hashlib.sha256()
    with open(file_path, "rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def check_apks_uniqueness_in_folders(root_folder):
    results = []
    for folder_name, subfolders, _ in os.walk(root_folder):
        for subfolder in subfolders:
            folder_path = os.path.join(folder_name, subfolder)
            apk_hashes = set()
            for _, _, files in os.walk(folder_path):
                for file_name in files:
                    if file_name.endswith(".apk"):
                        file_path = os.path.join(folder_path, file_name)
                        sha256_hash = calculate_sha256(file_path)
                        is_unique = sha256_hash not in apk_hashes
                        apk_hashes.add(sha256_hash)
                        # Device type column based on APK file name
                        device_type = ""
                        if file_name.endswith("watch.apk"):
                            device_type = "watch"
                        elif file_name.endswith("phone.apk"):
                            device_type = "phone"
                        elif file_name.endswith("tv.apk"):
                            device_type = "tv"
                        results.append({"Folder": subfolder, "APK": file_name, "Is Unique": is_unique, "With Device": device_type})
            # Separator line
            results.append({"Folder": "------------------", "APK": "------------------", "Is Unique": "------------------", "With Device": "------------------"})
    return results

if __name__ == "__main__":
    root_folder = r"E:\watch"
    results = check_apks_uniqueness_in_folders(root_folder)
    df = pd.DataFrame(results)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    print(df)

    # export DataFrame to CSV file
    output_file = "output.csv"
    df.to_csv(output_file, index=False)

