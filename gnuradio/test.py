#!/usr/bin/env python3

from gnuradio import gr
from gnuradio import audio, analog
import time



class my_top_block(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)



        freq1 = 1000
        sample_rate = 32000
        ampl = 0.1

        src0 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, self.get_freq(), ampl)
        src1 = analog.sig_source_f(sample_rate, analog.GR_SIN_WAVE, 440, ampl)
        dst = audio.sink(sample_rate, "")
        self.connect(src0, (dst, 0))
        self.connect(src1, (dst, 1))


    def get_freq(self):
        return 1000

if __name__ == '__main__':
    try:
        my_top_block().run()
    except [[KeyboardInterrupt]]:
        pass