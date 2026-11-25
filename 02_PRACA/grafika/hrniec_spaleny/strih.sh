#!/bin/bash
# Reel „spálený hrniec“ 9:16, bez textu. Použitie: bash strih.sh  (z koreňa repozitára)
# Fotky: video_reel.py (pomalý zoom). Videá: výrez úsekov + zrýchlenie. Hudba: hudba.py.
set -e
D=02_PRACA/grafika/hrniec_spaleny; O=$D/01_originaly; T=$(mktemp -d)
foto() {  # foto <img> <dur> <z0> <z1> <výstup>
  echo "{\"scenes\":[{\"img\":\"$1\",\"dur\":$2,\"zoom\":[$3,$4],\"focus\":[0.5,0.5]}]}" > $T/s.json
  python3 02_PRACA/sijacie_stroje/video_reel.py $T/s.json $5; }
usek() {  # usek <video> <od> <do> <zrýchlenie> <výstup>
  ffmpeg -y -loglevel error -ss $2 -to $3 -i $1 -an -vf "setpts=PTS/$4,fps=30,scale=1080:1920,setsar=1" \
    -c:v libx264 -crf 18 -pix_fmt yuv420p $5; }
foto $O/1_pred_A.jpg 1.6 1.0 1.12 $T/01.mp4                  # spálené dno
usek $O/video1_pena_hubka.mp4 0 6.5 2.6 $T/02.mp4             # nástrek + pena
usek $O/video1_pena_hubka.mp4 9 20 3.2 $T/03.mp4              # drhnutie hubkou
usek $O/video2_drotenka_hubka.mp4 1 11 4.5 $T/04.mp4          # drôtenka
usek $O/video2_drotenka_hubka.mp4 20.2 22.6 1.2 $T/05.mp4     # špinavá hubka
foto $O/4_dno_zvonka.jpg 2.2 1.12 1.0 $T/06.mp4               # čisté dno
foto $O/5_dno_zvonka_bok.jpg 1.6 1.0 1.08 $T/07.mp4
for f in $T/0*.mp4; do echo "file '$f'"; done > $T/list.txt
ffmpeg -y -loglevel error -f concat -safe 0 -i $T/list.txt -an -vf "eq=contrast=1.06:saturation=1.1,fade=t=in:d=0.3" \
  -c:v libx264 -crf 20 -pix_fmt yuv420p $T/v.mp4
DUR=$(ffprobe -v error -show_entries format=duration -of csv=p=0 $T/v.mp4)
python3 02_PRACA/grafika/hytteservice/hudba.py $T/h.wav 20 >/dev/null
ffmpeg -y -loglevel error -i $T/v.mp4 -i $T/h.wav -map 0:v -map 1:a -c:v copy \
  -af "afade=t=out:st=$(echo "$DUR-1.5"|bc):d=1.5,loudnorm=I=-14:TP=-1.5" -c:a aac -b:a 192k -shortest \
  -movflags +faststart $D/hrniec_navrh2_1080x1920.mp4
rm -r $T; echo "hotovo: $DUR s"
