# encoding:utf-8
import sys
from config import conf, load_config
from channel import channel_factory
from common.log import logger

from plugins import *

def run():
    try:
        # load config
        name = 'wx'
        if len(sys.argv) > 1:
            name = sys.argv[1]
        
        load_config({"channel_type": name})
        
        # create channel
        channel_name=conf().get('channel_type', name)
        channel = channel_factory.create_channel(channel_name)
        if channel_name=='wx':
            PluginManager().load_plugins()

        # startup channel
        channel.startup()
    except Exception as e:
        logger.error("App startup failed!")
        logger.exception(e)

if __name__ == '__main__':
    run()