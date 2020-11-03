#!/usr/bin/env python2
# -*- coding: utf-8 -*-
##################################################
# GNU Radio Python Flow Graph
# Title: rx_test
# Author: CTS
# Generated: Thu Apr 30 17:52:51 2020
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

import os
import sys
sys.path.append(os.environ.get('GRC_HIER_PATH', os.path.expanduser('~/.grc_gnuradio')))

from PyQt4 import Qt
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
from rf_over_ip_source import rf_over_ip_source  # grc-generated hier_block
import ConfigParser
import epy_chdir  # embedded python module
import epy_mkfifo  # embedded python module
import sip
from gnuradio import qtgui


class rx_test(gr.top_block, Qt.QWidget):

    def __init__(self, config_file_path="./config.cfg", rx_frequency=900000000, server_ip="127.0.0.1", throttle=1, zmq_rx_timeout=1000):
        gr.top_block.__init__(self, "rx_test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("rx_test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "rx_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.config_file_path = config_file_path
        self.rx_frequency = rx_frequency
        self.server_ip = server_ip
        self.throttle = throttle
        self.zmq_rx_timeout = zmq_rx_timeout

        ##################################################
        # Variables
        ##################################################
        self.config_file = config_file = config_file_path
        self._server_port_base_config = ConfigParser.ConfigParser()
        self._server_port_base_config.read(config_file)
        try: server_port_base = self._server_port_base_config.getint('main', "server_port_base")
        except: server_port_base = 10000
        self.server_port_base = server_port_base
        self._server_bw_per_port_config = ConfigParser.ConfigParser()
        self._server_bw_per_port_config.read(config_file)
        try: server_bw_per_port = self._server_bw_per_port_config.getint('main', "server_bw_per_port")
        except: server_bw_per_port = 1000000
        self.server_bw_per_port = server_bw_per_port
        self.server_port = server_port = int(server_port_base + (rx_frequency / server_bw_per_port))
        self._server_address_format_config = ConfigParser.ConfigParser()
        self._server_address_format_config.read(config_file)
        try: server_address_format = self._server_address_format_config.get("main", "server_address_format")
        except: server_address_format = "tcp://%s:%d"
        self.server_address_format = server_address_format
        self.server_address = server_address = server_address_format % (server_ip, server_port) if server_address_format != "" else ""
        self.samp_rate = samp_rate = 500000
        self.fifo = fifo = os.path.join(os.path.expanduser('~'), "cts.fifo")

        ##################################################
        # Blocks
        ##################################################
        self.rf_over_ip_source_0 = rf_over_ip_source(
            parent=self if 'self' in locals() else None,
            rx_frequency=rx_frequency,
            samp_rate=samp_rate,
            server_address_format=server_address_format,
            server_bw_per_port=server_bw_per_port,
            server_ip=server_ip,
            server_port_base=server_port_base,
            throttle=throttle,
            zmq_rx_timeout=zmq_rx_timeout,
        )
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-2, 2)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(True)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)

        if not True:
          self.qtgui_time_sink_x_0.disable_legend()

        labels = ['', '', '', '', '',
                  '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]

        for i in xrange(2):
            if len(labels[i]) == 0:
                if(i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_grid_layout.addWidget(self._qtgui_time_sink_x_0_win)



        ##################################################
        # Connections
        ##################################################
        self.connect((self.rf_over_ip_source_0, 0), (self.qtgui_time_sink_x_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "rx_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_config_file_path(self):
        return self.config_file_path

    def set_config_file_path(self, config_file_path):
        self.config_file_path = config_file_path
        self.set_config_file(self.config_file_path)

    def get_rx_frequency(self):
        return self.rx_frequency

    def set_rx_frequency(self, rx_frequency):
        self.rx_frequency = rx_frequency
        self.set_server_port(int(self.server_port_base + (self.rx_frequency / self.server_bw_per_port)))
        self.rf_over_ip_source_0.set_rx_frequency(self.rx_frequency)

    def get_server_ip(self):
        return self.server_ip

    def set_server_ip(self, server_ip):
        self.server_ip = server_ip
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")
        self.rf_over_ip_source_0.set_server_ip(self.server_ip)

    def get_throttle(self):
        return self.throttle

    def set_throttle(self, throttle):
        self.throttle = throttle
        self.rf_over_ip_source_0.set_throttle(self.throttle)

    def get_zmq_rx_timeout(self):
        return self.zmq_rx_timeout

    def set_zmq_rx_timeout(self, zmq_rx_timeout):
        self.zmq_rx_timeout = zmq_rx_timeout
        self.rf_over_ip_source_0.set_zmq_rx_timeout(self.zmq_rx_timeout)

    def get_config_file(self):
        return self.config_file

    def set_config_file(self, config_file):
        self.config_file = config_file
        self._server_port_base_config = ConfigParser.ConfigParser()
        self._server_port_base_config.read(self.config_file)
        if not self._server_port_base_config.has_section('main'):
        	self._server_port_base_config.add_section('main')
        self._server_port_base_config.set('main', "server_port_base", str(None))
        self._server_port_base_config.write(open(self.config_file, 'w'))
        self._server_bw_per_port_config = ConfigParser.ConfigParser()
        self._server_bw_per_port_config.read(self.config_file)
        if not self._server_bw_per_port_config.has_section('main'):
        	self._server_bw_per_port_config.add_section('main')
        self._server_bw_per_port_config.set('main', "server_bw_per_port", str(None))
        self._server_bw_per_port_config.write(open(self.config_file, 'w'))
        self._server_address_format_config = ConfigParser.ConfigParser()
        self._server_address_format_config.read(self.config_file)
        if not self._server_address_format_config.has_section("main"):
        	self._server_address_format_config.add_section("main")
        self._server_address_format_config.set("main", "server_address_format", str(None))
        self._server_address_format_config.write(open(self.config_file, 'w'))

    def get_server_port_base(self):
        return self.server_port_base

    def set_server_port_base(self, server_port_base):
        self.server_port_base = server_port_base
        self.set_server_port(int(self.server_port_base + (self.rx_frequency / self.server_bw_per_port)))
        self.rf_over_ip_source_0.set_server_port_base(self.server_port_base)

    def get_server_bw_per_port(self):
        return self.server_bw_per_port

    def set_server_bw_per_port(self, server_bw_per_port):
        self.server_bw_per_port = server_bw_per_port
        self.set_server_port(int(self.server_port_base + (self.rx_frequency / self.server_bw_per_port)))
        self.rf_over_ip_source_0.set_server_bw_per_port(self.server_bw_per_port)

    def get_server_port(self):
        return self.server_port

    def set_server_port(self, server_port):
        self.server_port = server_port
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")

    def get_server_address_format(self):
        return self.server_address_format

    def set_server_address_format(self, server_address_format):
        self.server_address_format = server_address_format
        self.set_server_address(self.server_address_format % (self.server_ip, self.server_port) if self.server_address_format != "" else "")
        self.rf_over_ip_source_0.set_server_address_format(self.server_address_format)

    def get_server_address(self):
        return self.server_address

    def set_server_address(self, server_address):
        self.server_address = server_address

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.rf_over_ip_source_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)

    def get_fifo(self):
        return self.fifo

    def set_fifo(self, fifo):
        self.fifo = fifo


def argument_parser():
    parser = OptionParser(usage="%prog: [options]", option_class=eng_option)
    parser.add_option(
        "", "--config-file-path", dest="config_file_path", type="string", default="./config.cfg",
        help="Set Configuration file path [default=%default]")
    parser.add_option(
        "", "--rx-frequency", dest="rx_frequency", type="long", default=900000000,
        help="Set RX Frequency [default=%default]")
    parser.add_option(
        "", "--server-ip", dest="server_ip", type="string", default="127.0.0.1",
        help="Set Server IP [default=%default]")
    parser.add_option(
        "", "--throttle", dest="throttle", type="intx", default=1,
        help="Set Throttle [default=%default]")
    parser.add_option(
        "", "--zmq-rx-timeout", dest="zmq_rx_timeout", type="intx", default=1000,
        help="Set ZMQ RX Timeout [default=%default]")
    return parser


def main(top_block_cls=rx_test, options=None):
    if options is None:
        options, _ = argument_parser().parse_args()

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls(config_file_path=options.config_file_path, rx_frequency=options.rx_frequency, server_ip=options.server_ip, throttle=options.throttle, zmq_rx_timeout=options.zmq_rx_timeout)
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
