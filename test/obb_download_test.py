import os
import shutil

from gpapi.googleplay import GooglePlayAPI

import argparse

ap = argparse.ArgumentParser(description='Test download of expansion files')
ap.add_argument('-e', '--email', dest='email', help='google username')
ap.add_argument('-p', '--password', dest='password', help='google password')

args = ap.parse_args()

server = GooglePlayAPI('it_IT', 'Europe/Rome')

# LOGIN
print('\nLogging in with email and password\n')
server.login(args.email, args.password, None, None)

# DOWNLOADING

# Create downloads directory, if already exists then delete it with related contents
if os.path.exists("downloads"):
    shutil.rmtree("downloads")

os.makedirs("downloads")

# Google play application package id(s)
docids = []
package_id_file = 'package_id.txt'
with open(package_id_file, 'r') as file:
    docids = [line.strip() for line in file]

count = 1;
for docid in docids:
    print('\nDownloading apk '+str(count) + "\n")

    download = server.download(docid, expansion_files=True)

    # Download APK file(s)
    apk_path = os.path.join("downloads", download['docId'] + '.apk')
    with open(apk_path, 'wb') as apk_file:
        for chunk in download.get('file').get('data'):
            apk_file.write(chunk)

    # Download additional file(s)
    print('\nDownloading additional files ' + str(count) + "\n")

    for obb in download['additionalData']:
        obb_folder = os.path.join("downloads", download['docId'] + "_obb")
        if not os.path.exists(obb_folder):
            os.makedirs(obb_folder)

        obb_name = obb['type'] + '.' + str(obb['versionCode']) + '.' + download['docId'] + '.obb'
        obb_path = os.path.join(obb_folder, obb_name)

        with open(obb_path, 'wb') as obb_file:
            for chunk in obb.get('file').get('data'):
                obb_file.write(chunk)

    count+=1;

print('\nDownload successful\n')
