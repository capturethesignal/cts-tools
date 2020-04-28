# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: RF Over IP Source
# Author: Jonathan Andersson
# Generated: Tue Apr 28 17:01:46 2020
##################################################


import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from gnuradio import blocks
from gnuradio import gr
from gnuradio import zeromq
from gnuradio.filter import firdes
from grc_gnuradio import blks2 as grc_blks2
from tags_to_vars import tags_to_vars  # grc-generated hier_block


class rf_over_ip_source(gr.hier_block2):

    def __init__(self, parent=self if 'self' in locals() else None, rx_frequency=1000000, samp_rate=500000, server_address_format="tcp://%s:%d", server_bw_per_port=1000000, server_ip='', server_port_base=10000, throttle=1, zmq_rx_timeout=100):
        gr.hier_block2.__init__(
            self, "RF Over IP Source",
            gr.io_signature(0, 0, 0),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.parent = parent
        self.rx_frequency = rx_frequency
        self.samp_rate = samp_rate
        self.server_address_format = server_address_format
        self.server_bw_per_port = server_bw_per_port
        self.server_ip = server_ip
        self.server_port_base = server_port_base
        self.throttle = throttle
        self.zmq_rx_timeout = zmq_rx_timeout

        ##################################################
        # Variables
        ##################################################
        self.server_port = server_port = int(server_port_base + (rx_frequency / server_bw_per_port))
        self.server_address = server_address = server_address_format % (server_ip, server_port) if server_address_format != "" else ""

        ##################################################
        # Blocks
        ##################################################
        self.zeromq_sub_source_0 = zeromq.sub_source(gr.sizeof_gr_complex, 1, server_address, zmq_rx_timeout, True, -1)
        self.tags_to_vars_0 = tags_to_vars(
            parent=parent,
            tag_map={"rx_rate": "set_samp_rate(value)"},
        )
        self.blocks_throttle_0_0 = blocks.throttle(gr.sizeof_gr_complex*1, samp_rate,False)
        self.blks2_selector_0 = grc_blks2.selector(
        	item_size=gr.sizeof_gr_complex*1,
        	num_inputs=2,
        	num_outputs=1,
        	input_index=0 if throttle else 1,
        	output_index=0,
        )

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blks2_selector_0, 0), (self, 0))
        self.connect((self.blocks_throttle_0_0, 0), (self.blks2_selector_0, 0))
        self.connect((self.zeromq_sub_source_0, 0), (self.blks2_selector_0, 1))
        self.connect((self.zeromq_sub_source_0, 0), (self.blocks_throttle_0_0, 0))
        self.connect((self.zeromq_sub_source_0, 0), (self.tags_to_vars_0, 0))

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent
        self.tags_to_vars_0.set_parent(self.parent)

    def get_rx_frequency(self):
        return self.rx_frequency

    def set_rx_frequency(self, rx_frequency):
        self.rx_frequency = rx_frequency
        self.set_server_port(int(self.server_port_base + (self.rx_frequency / self.server_bw_per_port)))

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.blocks_throttle_0_0.set_sample_rate(self.samp_rate)

    def get_server_address_format(self):
        return self.server_address_format

    def set_server_address_format(self, server_address_format):
        self.server_address_format = server_address_format
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")

    def get_server_bw_per_port(self):
        return self.server_bw_per_port

    def set_server_bw_per_port(self, server_bw_per_port):
        self.server_bw_per_port = server_bw_per_port
        self.set_server_port(int(self.server_port_base + (self.rx_frequency / self.server_bw_per_port)))

    def get_server_ip(self):
        return self.server_ip

    def set_server_ip(self, server_ip):
        self.server_ip = server_ip
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")

    def get_server_port_base(self):
        return self.server_port_base

    def set_server_port_base(self, server_port_base):
        self.server_port_base = server_port_base
        self.set_server_port(int(self.server_port_base + (self.rx_frequency / self.server_bw_per_port)))

    def get_throttle(self):
        return self.throttle

    def set_throttle(self, throttle):
        self.throttle = throttle
        self.blks2_selector_0.set_input_index(int(0 if self.throttle else 1))

    def get_zmq_rx_timeout(self):
        return self.zmq_rx_timeout

    def set_zmq_rx_timeout(self, zmq_rx_timeout):
        self.zmq_rx_timeout = zmq_rx_timeout

    def get_server_port(self):
        return self.server_port

    def set_server_port(self, server_port):
        self.server_port = server_port
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")

    def get_server_address(self):
        return self.server_address

    def set_server_address(self, server_address):
        self.server_address = server_address
