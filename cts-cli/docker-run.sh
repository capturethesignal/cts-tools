#! /bin/bash

CMD=${1:-/bin/bash}
IMAGE="phretor/gnuradio-mini:myriadrf"

docker pull ${IMAGE}
docker run \
    -it --rm \
    -v "$(pwd):/root/" \
    -w /root/ \
    ${IMAGE} \
    $CMD