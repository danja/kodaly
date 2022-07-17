**2022-07-17**

I set train.py running yesterday, still going today...

main
p = argparse.ArgumentParser()
p.add_argument("--seed", default=0, type=int)
p.add_argument("--trials", default=15, type=int)
p.add_argument("--epochs", default=150, type=int)
p.add_argument("--kernel_size", default=5, type=int)
p.add_argument("--gpu", default=0, type=int)
p.add_argument("--logdir", default="temp")
args = p.parse_args()
...

def run(p_seed=0, p_epochs=150, p_kernel_size=5, p_logdir="temp"):

**2022-07-16**

I felt like I was making progress on Python/OpenCV/QT image capture app, but kept running into system problems, generally Wayland-related.

So to avoid frustration, I'm going to flip to Javascript in the browser.

I've got xampp running on localhost, pop in a pointer to my working dir :

sudo ln -s /home/danny/micros/kodaly /opt/lampp/htdocs/kodaly

not sure if necessary, but I added

brave://flags/#unsafely-treat-insecure-origin-as-secure

really good progress!!!!!

mostly working

---

Installed PyTorch (CPU-only) according to : https://pytorch.org/get-started/locally/

pip3 install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cpu

pip install torch-summary

had to tweak train.py code, had a bit to exit if no GPU

running

time python3 train.py --seed=0 --trial=1 --kernel_size=5 --gpu=0 --logdir=modelM5

(trial=1, not 10 as in docs)

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
