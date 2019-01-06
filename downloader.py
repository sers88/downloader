import requests

for number in range(610, 631):
    urlop = 'http://archive.rucast.net/radio-t/media/rt_podcast' + str(number) + '.mp3'
    response = requests.get(urlop)
    podcast = response.content
    namefile = 'rt_podcast' + str(number) + '.mp3'
    fout = open(namefile, 'xb')
    fout.write(podcast)
    fout.close()

