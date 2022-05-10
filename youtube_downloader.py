# coding: utf-8
# use python3
from pytube import YouTube
import pandas as pd
import os

BASE_URL = 'https://www.youtube.com/watch?v='


def get_downloadURLSet(filename):
    URL_set = set()
    with open(filename) as f:
        for eachURL in f.readlines():
            eachURL = eachURL.rstrip('\n')
            URL_set.add(BASE_URL + eachURL)
            #print(eachURL)
    return URL_set



def download_video(downloadURLSet):
    videoIDlist_downloaded = []
    if len(downloadURLSet) == 0:
        print("no video to download")
        return
    current_number = 0
    for downloadURL in downloadURLSet:
        #print(1)
        print(downloadURL)
        try:
            yt = YouTube(downloadURL)
        except:
            print("Some thing wrong about the authority!")
            continue
        name = yt.title
        print("Now is loading %s------------>" % name)
        stream = yt.streams.filter(file_extension='mp4').first()
        stream.download('./videos_covidTest_nov')
        os.rename(os.path.join('./videos_covidTest_nov', yt.streams.first().default_filename), os.path.join('./videos_covidTest_nov', downloadURL.replace(BASE_URL, '')+'.mp4'))
        print("--------------->%s is loaded!" % name)
        videoIDlist_downloaded.append(downloadURL.replace(BASE_URL, ''))
        #current_number += 1
        # if current_number == 5:
        #     break
    #pd.DataFrame(videoIDlist_downloaded).to_csv('videoIDlist_downloaded_nov.txt', sep='\t', index=False)


# Because of authority issue some video cannot be downloaded
def get_ID_download(filename):
    videoIDlist_downloaded=[]
    with open(filename) as f:
        for videoID in f.readlines():
            eachURL =BASE_URL + videoID.strip()
            try:
                yt = YouTube(eachURL)
            except:
                #print("Something is wrong about the authority!")
                continue
            videoIDlist_downloaded.append(videoID.strip())

    #pd.DataFrame(videoIDlist_downloaded).to_csv('videoIDlist_downloaded_nov.txt', sep='\t', index=False)

def main():
    URL_set = get_downloadURLSet('videoIDlist_covidTest_nov.txt')
    print(len(URL_set))
    download_video(URL_set)



if __name__ == '__main__':
    main()
