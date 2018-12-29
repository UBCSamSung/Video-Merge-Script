mkdir intermediate
if not exist output mkdir output
ffmpeg -i input\1.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate\1.ts
ffmpeg -i input\2.mp4 -c copy -bsf:v h264_mp4toannexb -f mpegts intermediate\2.ts
ffmpeg -i "concat:intermediate\1.ts|intermediate\2.ts" -c copy -bsf:a aac_adtstoasc output\2018-12-29-011351.mp4
rmdir  /s /q intermediate
if exist intermediate rmdir  /s /q intermediate
