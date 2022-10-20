import logging


def get_logger(module_name, level=logging.INFO):
    root_logger = logging.getLogger(module_name)
    root_logger.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    root_logger.addHandler(handler)
    return root_logger
