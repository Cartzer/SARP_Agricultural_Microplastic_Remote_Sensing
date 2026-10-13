print('need to create a new file')
filename = input('New file name:\n')
file = filename+'.txt'
f = open(file,'x')
# creating a new file under the name the user inputs
f = open(file,'r+')
shortWave = int(input('Shortest Wavelength:''\n'))
longWave = int(input('Longest Wavelength:''\n'))
waveStep = int(input('Wavelength Step:''\n'))
# prompting the user for the wavelength range and the step (will change with instrument)
wavlengths = [str(i)+'\n' for i in range(shortWave,longWave,waveStep)]
# creates a list of the wavelengths with '\n' to create new files
print(wavlengths)
f.writelines(wavlengths)
f.close()
# writing the data onto the file
print('file created!')
