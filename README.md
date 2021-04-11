# Face Detection

## Step 0: Download The Project
Run this command in Terminal/Command Prompt to download the code:
```
git clone -b master https://github.com/ekinkaradag/face-detection.git
```

<hr/>
<br/>

## Step 1: Install The Requirements
Navigate to the folder:
```
cd face-detection
```

Run this command to be able to use OpenCV.
```
python3 -m pip install -r requirements.txt
```

<hr/>
<br/>

## Step 2: Run

### Detect Over Webcam

Run this command to detect the faces over your webcam:
```
python3 detect_over_webcam.py
```

### Detect From Photo

If you want to save the image of the photo with the detected faces, run this (Replace <code>photo.png</code> with the photo you want to insert, and replace <code>outputImage.png</code> with a filename of your choice):
```
python3 detect_from_photo.py photo.png outputImage.png
```
<br/>

You don't necessarily have to save the output file. If you just want to see the results and don't want to save it to your disk, run this (Replace <code>photo.png</code> with the photo you want to insert):
```
python3 detect_from_photo.py photo.png
```