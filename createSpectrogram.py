import matplotlib.pyplot as plt
import librosa.display 
# from scipy.io import wavfile
import os


genres = ["blues", "classical", "country", "disco",
          "hiphop", "jazz", "metal", "pop", "reggae", "rock"]

for i in range(len(genres)):
    pathName = os.path.join("img_data/", genres[i])
    if not os.path.isdir(pathName):
        print("Creating Folders for Spectrogram Images..."+genres[i]+"\n")
        print("Path name for spectrogram images"+ genres[i]+ "is: "+ pathName)
        os.makedirs(pathName)


for i in range(len(genres)):
    genrePath = genres[i]+"/"
    genreDirectory = os.path.join("genres_wav/", genrePath)
    fileName = os.listdir(genreDirectory)
    print("Creating Spectrogram Images for "+genres[i]+"..."+"\n")
    for y in range(len(fileName)):
        wavFile = os.path.join(genreDirectory, fileName[y])
        # print("WaveFile:", wavFile)

        # Load wave file and separate it to sample rate(sr) and audio time series(y)
        y, sr = librosa.load(wavFile, mono=True)
        X = librosa.stft(y)
        Xdb = librosa.amplitude_to_db(abs(X))
        plt.figure(figsize=(14, 5))
        # Convert the y-axis to a log to cover the bottom part of the frequency,
        # Where all the action is happening
        librosa.display.specshow(Xdb, sr=sr, x_axis='time', y_axis='log')
        # plt.title(genres[i])
        plt.colorbar()

        splicedName = " "
        # For Blues, Disco, Metal
        if (i == 0 or i == 3 or i == 6):
            splicedName = wavFile[17:-4]

        # For Classical
        elif (i == 1):
            splicedName = wavFile[21:-4]

        # For Country
        elif(i == 2):
            splicedName = wavFile[19:-4]

        # For Hiphop and Reggae
        elif(i == 4 or i == 8):
            splicedName = wavFile[18:-4]

        # For Jazz and Rock
        elif(i == 5 or i == 9):
            splicedName = wavFile[16:-4]

        # For Pop
        elif(i == 7):
            splicedName = wavFile[15:-4]

        plt.title(splicedName)
        splicedName.strip('.')
        splicedName = splicedName + ".png"
        pathName = os.path.join("./img_data/", genrePath)
        imagePath = os.path.join(pathName, splicedName)
        print("Path for "+splicedName+" is: "+imagePath)
        plt.savefig(imagePath, bbox_inches = 'tight')
        plt.close()