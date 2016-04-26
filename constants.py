# -*- coding: utf-8 -*-

LOCAL_T_MAX = 5 # repeat step size
RMSP_EPSILON = 1e-10 # epsilon parameter for RMSProp
CHECKPOINT_DIR = 'checkpoints'
LOG_FILE = 'tmp/a3c_log'
INITIAL_ALPHA_LOW = 1e-4    # log_uniform low limit for learning rate
INITIAL_ALPHA_HIGH = 1e-2   # log_uniform high limit for learning rate

PARALLEL_SIZE = 8 # parallel thread size
ROM = "pong.bin"     # action size = 3

ACTION_SIZE = 4 # action size

CHECKPOINT_DIR = 'checkpoints'

INITIAL_ALPHA_LOW = 1e-4    # log_uniform low limit for learning rate
INITIAL_ALPHA_HIGH = 1e-2   # log_uniform high limit for learning rate
INITIAL_ALPHA_LOG_RATE = 1.0 # log_uniform interpolate rate for learning rate
MAX_TIME_STEP = 100000 # 

GAMMA = 0.95 # discount factor for rewards
ENTROPY_BETA = 0.1 # entropy regurarlization constant
GRAD_NORM_CLIP = 40.0 # gradient norm clipping
