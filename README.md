# CTS client tools (CLI)

These are client tools used to connect to the [CTS](https://trendmicro.com/cts) infrastructure and receive RF data (IQ samples) over IP. They need a working GNU Radio 3.7 installation,  they're headless, and require no configuration file. We tested them with GNU Radio 3.7.14.

# Build (with Docker)
```bash
$ cd cts-cli/
$ ./docker-run.sh 'make all'
```

# Build on your Host (requires working GNU Radio 3.7)
```bash
$ cd cts-cli/
$ make all
```

Should you encounter **build errors on GNURadio 3.8**, please [check this out](https://github.com/gnuradio/gnuradio/issues/2763), or just use one of the provided VMs (they're tested). The cause is unknown, but a workaround exists (comment out `global_blocks_path` in `~/.gnuradio/grc.conf`).

# Usage Help
```bash
$ python rx_to_fifo.py --help
Tags to Var imported
FIFO already exists (not creating): /path/to/cts.fifo
Usage: rx_to_fifo.py: [options]

Options:
  -h, --help            show this help message and exit
  --rx-frequency=RX_FREQUENCY
                        Set RX Frequency [default=900000000]
  --server-ip=SERVER_IP
                        Set Server IP [default=127.0.0.1]
  --server-port-base=SERVER_PORT_BASE
                        Set Server Port Base [default=10000]
  --throttle=THROTTLE   Set Throttle [default=1]
  --zmq-rx-timeout=ZMQ_RX_TIMEOUT
                        Set ZMQ RX Timeout [default=100]
```

# Start Receiver
```bash
$ python rx_to_fifo.py                              \
  --server-ip=<this is given by the organizers>     \
  --rx-frequency=<each challenge has its own frequency>
Tags to Var imported
Tags to Var initialized

Created FIFO: /path/to/cts.fifo
IMPORTANT: Before you can see the source sample rate, you must start consuming samples from the FIFO
...
```

Check that you can receive at least one sample:

```bash
$ cat /path/to/cts.fifo > /dev/null
```

And you should now see the original signal's sample rate reported on the standard output:

```bash
...continued from above...

rx_rate = 128000.0
```

**IMPORTANT:** Each signal has it's own sample rate! Always check the reported sample rate before you start working on a signal. You can kill and restart the `rx_to_fifo.py` script as many times as you need (especially if it appears dead).

# Use with Docker
IQ samples are written to a named pipe (the FIFO file), which is an OS-dependent beast. In theory, you could run the 'rx_to_fifo.py' receiver within a Docker container and consume IQ-samples from *outside* the Docker container. However, this will work only if the host operating system is the same of the container operating system (i.e., Linux). We tried with a macOS host: didn't work!

```bash
$ ./docker-run.sh 'python rx_to_fifo.py                              \
  --server-ip=<this is given by the organizers>     \
  --rx-frequency=<each challenge has its own frequency>'
```

And then you can use `./cts.fifo` as any other named pipe (FIFO), e.g.
```bash
$ dd if=cts.fifo of=samples.raw bs=2048 count=1000
```

This will not work on any non-Linux host OS (because FIFOs are OS-specific) but a trick would be to use a second container that proxies that FIFO to a TCP socket (using `socat`), expose that port to the host, and then use `socat` on the host to re-proxy from the exposed port back to a file. Not clean, but should work.

Alternatively, simply use `dd` or `cat`:

```bash
$ ./docker-run.sh 'dd if=cts.fifo of=samples.raw bs=2048 count=1000'
```

The resulting `samples.raw` file can then be read directly into tools like URH.

# Receive with SDR Tools
Now you can consume RF data (IQ samples) from the FIFO. For example, with GQRX you can use the following device string:

```
file=/path/to/cts.fifo,freq=0,rate=<sample rate>,repeat=false,throttle=false
```

Again, you can keep a local copy of a the IQ samples of the signal by redirecting the output of the FIFO to your favorite file.

# Getting Build Errors?
You may get compilation errors, which actually don't block the build process. 

Should you encounter **build errors on GNURadio 3.8**, please [check this out](https://github.com/gnuradio/gnuradio/issues/2763), or just use one of the provided VMs (they're tested). The cause is unknown, but a workaround exists (comment out `global_blocks_path` in `~/.gnuradio/grc.conf`).

Other errors could be ignored: what really matters is the final `rx_to_fifo.py` file. If that's there and it loads without errors, you're good to go.

```bash
$ ls -lah *.py
ls: cannot access '*.py': No such file or directory

$ make
rm -rf *.pyc
rm -rf epy_*.py
for grc in tags_to_vars rx_to_fifo; do \
  rm -rf $grc.py; \
done
rm -rf build
rm -rf __pycache__
for grc in tags_to_vars rx_to_fifo; do \
  grcc -d ./ $grc.grc; \
done
Unhandled exception in thread started by <bound method Thread.__bootstrap of <Thread(Thread-1, stopped daemon 139634459854592)>>
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 774, in __bootstrap
    self.__bootstrap_inner()
  File "/usr/lib/python2.7/threading.py", line 814, in __bootstrap_inner
    (self.name, _format_exc()))
  File "/usr/lib/python2.7/traceback.py", line 241, in format_exc
    etype, value, tb = sys.exc_info()
AttributeError: 'NoneType' object has no attribute 'exc_info'
FIFO already exists: /home/user/cts.fifo
FIFO already exists: /home/user/cts.fifo
>>> Warning: This flow graph may not have flow control: no audio or RF hardware blocks found. Add a Misc->Throttle block to your flow graph to avoid CPU congestion.
Unhandled exception in thread started by <bound method Thread.__bootstrap of <Thread(Thread-1, stopped daemon 139966222206720)>>
Traceback (most recent call last):
  File "/usr/lib/python2.7/threading.py", line 774, in __bootstrap
    self.__bootstrap_inner()
  File "/usr/lib/python2.7/threading.py", line 814, in __bootstrap_inner
    (self.name, _format_exc()))
  File "/usr/lib/python2.7/traceback.py", line 241, in format_exc
    etype, value, tb = sys.exc_info()
AttributeError: 'NoneType' object has no attribute 'exc_info'

$ ls -lah *.py
-rw-rw-r-- 1 user user   93 Oct 15 15:19 epy_chdir.py
-rw-rw-r-- 1 user user  384 Oct 15 15:19 epy_mkfifo.py
-rw-rw-r-- 1 user user 1.6K Oct 15 15:18 epy_tags_to_vars.py
-rwxrwxr-- 1 user user  17K Oct 15 15:19 rx_to_fifo.py
```

Should you encounter blocking errors, just open an issue in or [contact us](https://trendmicro.com/cts/).
