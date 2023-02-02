## PICAXE 18M2 Microcontroller Emulator
import time
import keyboard as k
class PicAxe():
    def __init__(self):
        print("PicAxe turned on!")
        # initialise arrays to store pin states
        self.inputs = [0,0,0]
        self.outputs = [0,0,0,0,0,0,0,0]
        # add hotkeys for inputs and outputs
        self._add_pins(["0","1","2"])

    
    def _add_pins(self, pins):
        # cycle through pins and add hotkeys
        for num, pin in enumerate(pins):   
            k.add_hotkey(pin, self._toggle_state, args=(num,))

            
    def _toggle_state(self, num):
            self.inputs[num] = 0 if self.inputs[num] == 1 else 1
            print(f"Input {num} has been toggled. Now {self.inputs[num]}")

    # change the state of a pin
    def _change_state(self, num, state):
        self.outputs[num] = state
        print(f"Pin {num} changed to {state}")
    # wrappers for _change_state
    def on(self, num):
        self._change_state(num, 1)  
    def off(self, num):
        self._change_state(num, 0)
        
    # delay for a number of milliseconds. using millis to match picaxe   
    def delay(self, millis):
        time.sleep(millis/1000)

    def stop():
        print("PicAxe shut down.")
        k.unhook_all_hotkeys()
