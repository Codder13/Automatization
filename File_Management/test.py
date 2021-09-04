with open('ex.txt', 'r') as file:
    images = file.readline()
    text = file.readline()
    videos = file.readline()
    sounds = file.readline()
    applications = file.readline()
    codes = file.readline()
    zip_files = file.readline()

extensions = [images, text, videos, sounds, applications, codes, zip_files]

for i, j in enumerate(extensions):

    j = j.split(', ')
    j[0] = j[0].split('= ')[1]
    j[-1] = j[-1].split('\n')[0]
    extensions[i] = j

print(extensions)


