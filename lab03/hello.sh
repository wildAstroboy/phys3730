#!/bin/sh
echo "Hello, world."
if [ $# != 0 ] ; then
    echo "and hello $*!"
fi
