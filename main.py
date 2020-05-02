

#importing the package to identify operating system
import os







#writing the function to make folder with check to not duplicate same folder
def createIfNotExists(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

#function to move files in to folder
def move(folderName,files):
    for file in files:
        os.replace(file,f"{folderName}/{file}")

files = os.listdir()
files.remove("main.py")
#print(files)

createIfNotExists('Images')
createIfNotExists('Docs')
createIfNotExists('Media')
createIfNotExists('Others')


imgExts = [".png", ".jpg", ".jpeg"]
images = [file for file in files if os.path.splitext(file)[1].lower() in imgExts ]

docExts = [".txt",".docx",".doc",".pdf"]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docExts]

mediaExts = [".mp4",".mp3",".pptx",".ppt"]
medias = [file for file in files if os.path.splitext(file)[1].lower() in mediaExts]
#print(medias)


others = []
for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in mediaExts) and (ext not in docExts) and (ext not in imgExts) and os.path.isfile(file):
        others.append(file)

print(others)
move("Images",images)
move("Docs",docs)
move("Media",medias)
move("Others",others)
