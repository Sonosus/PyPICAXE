# PyPICAXE
An emulator for the PICAXE 18M2 microcontroller, designed for teaching beginners before moving on to using real BASIC.

## Installation

Download the repository's ZIP file (green button) and extract it to a new project folder.

Run the command `pip install keyboard` 

## Examples
At the start of any project you'll want:
```python
## import the library
import picaxe
## create a virtual microcontrolller
mc = picaxe.PicAxe()

```

Now you have an instance of `mc` you can use the various input and output commands as well as the usual Python loops and functions to control the virtual microcontroller.

```python
mc.on(0) # turn on output 0
mc.delay(1000) # wait 1 second
mc.off(0) # turn off output 0

print(mc.inputs[2]) # get the state of an input pin

## while input 0 is off, check if it is pressed, and turn on output 1
while mc.inputs[0] == 0:
  if mc.inputs[0] == 1:
    mc.on(1)
mc.delay(2000) # after a delay, turn off output 1
mc.off(1)

mc.stop()
```
It is important to run `mc.stop()` at the end of your script to safely disable the keybindings.
