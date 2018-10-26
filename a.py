import os, urllib
urllib.urlretrieve("https://apod.nasa.gov/apod/image/1810/HyperionGalaxies_ESO_6000.jpg","wall.jpg")
os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri /home/sanskari_purush/wall.jpg")
