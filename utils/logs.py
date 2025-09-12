import logging

def config_logs():

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        filename='app.log',
        filemode='w'
        )


def get_logger(name):
    return logging.getLogger(name)



