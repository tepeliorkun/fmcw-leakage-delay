import numpy as np
import time
from gnuradio import gr

class blk(gr.sync_block):  
    def __init__(self, duration=10):  
        gr.sync_block.__init__(
            self, 
            name='Timer',
            in_sig=[np.complex64],
            out_sig=[np.complex64]
        )
        self.duration = duration
        self.pass_data = True

    def work(self, input_items, output_items):
        if not hasattr(self, "start_time"):
            self.start_time = time.time()

        now = time.time()
        if now - self.start_time >= self.duration:
            self.pass_data = False

        if self.pass_data:
            output_items[0][:] = input_items[0]
            return len(output_items[0])
        else:
            return 0
