import sys
if sys.prefix == '/Users/ilangoldfein/dev/pid-bot/ros_ws/.pixi/envs/default':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/Users/ilangoldfein/dev/pid-bot/ros_ws/install/controller'
