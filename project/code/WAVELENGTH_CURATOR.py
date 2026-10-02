try:
    f = open('av5_wave.txt','r+')
    wavlengths = []
    shortWave = int(input('Shortest Wavelength:''\n'))
    longWave = int(input('Longest Wavelength:''\n'))
    waveStep = int(input('Wavelength Step:''\n'))
    for i in range(shortWave,longWave,waveStep):
        wavlengths.append(str(i)+'\n')
    print(wavlengths)
    f.writelines(wavlengths)
    f.close()
    print('file written!')
except:
    print('need to create a new file')
    filename = input('New file name:\n')
    file = filename+'.txt'
    f = open(file,'x')
    f = open(file,'r+')
    wavlengths = []
    shortWave = int(input('Shortest Wavelength:''\n'))
    longWave = int(input('Longest Wavelength:''\n'))
    waveStep = int(input('Wavelength Step:''\n'))
    for i in range(shortWave,longWave,waveStep):
        wavlengths.append(str(i)+'\n')
    print(wavlengths)
    f.writelines(wavlengths)
    f.close()
    print('file created!')
