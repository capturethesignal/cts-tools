"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

from __future__ import print_function
import numpy as np
from gnuradio import gr
import pmt

print("Tags to Var imported")

class blk(gr.basic_block):
    """Tags to Vars"""

    def __init__(self, parent=self if 'self' in locals() else None, tag_map={"rx_rate": "set_samp_rate(value)"}): # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.basic_block.__init__(
        #gr.sync_block.__init__(
            self,
            name='Tags to Vars',   # will show up in GRC
            in_sig=[np.complex64],
            out_sig=[]
        )
        # if an attribute with the same name as a parameter is found, a callback is registered (properties work, too).
        self.parent = parent
        self.tag_map = tag_map
        self.hist = {}
        #self.tag_map = {"rx_rate": "set_samp_rate(value)"}

        print("Tags to Var initialized\n\n\n")

        self.set_tag_propagation_policy(0) #gr_extras.TPP_DONT
        return

    def general_work(self, input_items, output_items): #basic_block
    #def work(self, input_items, output_items): #sync_block

        if self.parent is not None:
            packet_begin_tags = self.get_tags_in_window(0, 0, len(input_items[0]))
            for tag in packet_begin_tags:
                #offset = tag.offset
                key = pmt.symbol_to_string(tag.key)
                value = pmt.to_python(tag.value)
                if key in self.tag_map:
                    if key not in self.hist:
                        self.hist[key] = None
                    if value != self.hist[key]:
                        print(key, '=', value)
                        self.hist[key] = value
                    eval("self.parent.%s" % (self.tag_map[key]))

        self.consume_each(len(input_items[0]))
        return 0
