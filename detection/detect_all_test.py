import detection
import os

## list all pic in test
##python -u detection.py --img test/ae3.jpg --gpu 0 
## onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]

images = [ff for ff in os.listdir("test") if os.path.isfile(os.path.join("test",ff))]

for image in images:
    detection.detect('test/'+image)    

print images
