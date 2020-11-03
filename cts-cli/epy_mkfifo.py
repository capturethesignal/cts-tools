import os

path = os.path.join(os.path.expanduser('~'), "cts.fifo")

if not os.path.exists(path):
    try:
        os.mkfifo(path)
    except OSError, e:
        print("Cannot create FIFO '{}': {}".format(path, e))
    else:
        print("Created FIFO: {}".format(path))
        print("IMPORTANT: Before you can see the source sample rate, you must start consuming samples from the FIFO")
else:
    print("FIFO already exists (not creating): {}".format(path))
    print("IMPORTANT: Before you can see the source sample rate, you must start consuming samples from the FIFO")