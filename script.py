import os
import datetime
import time
import sys
encoding=sys.getfilesystemencoding()

sys.stdout = open("script.bat", "w", encoding='utf-8')

def main():
    # print("@echo off")
    intermediate_files=[]
    print('mkdir intermediate')
    print('if not exist output mkdir output')
    for file in os.listdir("input"):
        if not file.endswith(".mp4"):
            continue
        file_path=os.path.join("input", file)
        base_name=os.path.splitext(file)[0]
        intermediate_file=os.path.join("intermediate", "{}.ts".format(base_name))
        intermediate_files.append(intermediate_file)
        print("ffmpeg -i {} -c copy -bsf:v h264_mp4toannexb -f mpegts {}".format(file_path, intermediate_file))
    timestamp=time.strftime("%Y-%m-%d-%H%M%S")
    input_string='|'.join(intermediate_files)
    print('ffmpeg -i "concat:{}" -c copy -bsf:a aac_adtstoasc output\{}.mp4'.format(input_string,timestamp))
    print('rmdir  /s /q intermediate')
    print('if exist intermediate rmdir  /s /q intermediate')

if __name__ == "__main__":
    main()