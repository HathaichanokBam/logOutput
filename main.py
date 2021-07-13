import os
import time
import glob
import json

path = 'C:/Users/Administrator/Desktop/Logdevice01/01.CONF'  # config path
for filename in glob.glob(os.path.join(path, '*.json')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in read-only mode
        f2 = open(filename, "r")
        data = json.load(f2)
        input_path = data["INPUT_PATH"]
        output_path = data["OUTPUT_PATH"]
        isArchive = data["isARCHIVE"]
        if isArchive:
            archive_path = data["ARCHIVE_PATH"]
        f2.close()
    f.close()
filename_list = os.listdir(input_path)
prev_date = ''
for filename in glob.glob(os.path.join(input_path, '*.json')):
    with open(os.path.join(os.getcwd(), filename), 'r') as f:  # open in read-only mode
        print(filename)
        date = time.strftime('%Y-%m-%d', time.localtime(os.path.getmtime(filename)))
        date = date.replace("-", "")
        f2 = open(filename, "r")
        data = json.load(f2)
        if prev_date == '' or prev_date != date:
            with open(output_path + '\\' + date + '.json', 'w') as f3:
                json.dump(data, f3)
                f3.close()
            if isArchive:
                print(archive_path)
                if not os.path.exists(archive_path + '\\' + date):
                    os.makedirs(archive_path + '\\' + date)
        elif prev_date == date:
            with open(output_path + '\\' + date + '.json', 'a') as f3:
                f3.write("\n")
                json.dump(data, f3)
                f3.close()

        prev_date = date
        f2.close()
    f.close()
    print(filename_list)
    if isArchive:
        for i in filename_list:
            if filename.find('\\' + i) != -1:
                print(i)
                os.replace(filename, archive_path + '\\' + date + '\\' + i)
                break
        filename_list.remove(i)
