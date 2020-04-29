GRCS = rx_test rx_to_fifo tags_to_vars
HIERS = rf_over_ip_source

.PHONY: all
all: clean main

.PHONY: main
main:
	for grc in $(GRCS); do grcc -d ./ $$grc.grc ; done
	for hier in $(HIERS); do mv ${HOME}/.grc_gnuradio/$$hier.py ./ ; done

.PHONY: clean
clean:
	for hier in $(HIERS); do rm -rf ${HOME}/.grc_gnuradio/$$hier.py* ; done
	rm -rf *.fifo
	rm -rf *.py*
	rm -rf epy_*.py
	rm -rf build
	rm -rf __pycache__
