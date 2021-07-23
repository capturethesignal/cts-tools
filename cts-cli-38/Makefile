.PHONY: all
all: clean main

.PHONY: main
main:
	grcc tags_to_vars.grc
	grcc rf_over_ip_source.grc
	grcc rx_to_fifo.grc

.PHONY: clean
clean:
	for hier in $(HIERS); do rm -rf ${HOME}/.grc_gnuradio/$$hier.py* ; done
	rm -rf *.fifo
	rm -rf *.py*
	rm -rf epy_*.py
	rm -rf build
	rm -rf __pycache__
