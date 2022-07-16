**2022-07-16**

I felt like I was making progress on Python/OpenCV/QT image capture app, but kept running into system problems, generally Wayland-related.

So to avoid frustration, I'm going to flip to Javascript in the browser.

I've got xampp running on localhost, pop in a pointer to my working dir :

sudo ln -s /home/danny/micros/kodaly /opt/lampp/htdocs/kodaly

not sure if necessary, but I added

brave://flags/#unsafely-treat-insecure-origin-as-secure

copied demo from https://usefulangle.com/post/352/javascript-capture-image-from-camera

**2022-07-15**

Key Note
0 Do
1 Re
2 Mi
3 Fa
4 Sol
5 La
6 Ti

**2022-07-14**

Ok, got image capture from USB camera working:

python3 simple-cam-capture.py

Now need to wrap in a little UI.

Qt for Python packages appears to be

pip install pyside6

demo from https://doc.qt.io/qtforpython/quickstart.html

python3 hello-qt.py

works!

**2022-07-13**

[How to capture a image from webcam in Python?](https://www.geeksforgeeks.org/how-to-capture-a-image-from-webcam-in-python/)

pip install opencv-python

Hmm, seems I am running on anaconda3, it doesn't have the Wayland QT libs

not clear if Anaconda supports this. Trying

conda config --set auto_activate_base False

nope.

https://github.com/pyenv/pyenv

putting that on seems to have put me back to system python. Ok.

python3 capture.py

same problem ^^^

pip install opencv-python-headless

installed python3-qtpy

python3-opencv

still not quite there, so doing it from source

https://docs.opencv.org/4.x/d2/de6/tutorial_py_setup_in_ubuntu.html

ok, I needed to do

pip uninstall opencv-python-headless -y

but now that bit works!
