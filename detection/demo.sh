#!/usr/bin/env sh

export MXNET_ENGINE_TYPE=NaiveEngine
python -u detection.py --img test/ae3.jpg --gpu 0 
