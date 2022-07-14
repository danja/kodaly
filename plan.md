## Requirements/Plan

Get things working on desktop, later (if I have the energy), port to ESP32 CAM.

Python, PyTorch and/or TensorFlow

### Training Data

Need to be able to produce a **lot** of (labelled) hand signal images.

#### Make a little UI app :

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
