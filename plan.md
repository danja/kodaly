### Immediate TODOs

- figure out MNIST format
- write up
- get working on mobile

## Requirements/Plan

Get things working on desktop, later (if I have the energy), port to ESP32 CAM.

Browser Javascript for training data capture

Python, PyTorch and/or TensorFlow for machine learning

### Training Data

Need to be able to produce a **lot** of (labelled) hand signal images.

#### Make a little UI app : (mostly done)

- image area
- buttons : 'Prompt', 'Capture'

On clicking 'Prompt' :

- image area displays one of the 7 Kodaly hand shapes
- corresponding tone plays

On clicking 'Capture' :

- image captured from USB camera
- image saved with filename containing sol-fa label
- tone stopped
- image area displays captured image

#### Prepare data

Script to process images + labels into MNIST format

### Create model code

train with ^^

### Create runtime app

Maybe start with original MNIST, show handwritten digit to the camera
