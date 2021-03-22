import logging
from pathlib import Path
import inspect
import sys


def function_logger(file_level: str, console_level: str, logdirs=""):
    MIN_LEVEL = logging.DEBUG
    function_name = inspect.stack()[1][3]
    logger = logging.getLogger(function_name)
    logger.setLevel(MIN_LEVEL)  # By default, logs all messages

    logger.propagate = False
    ch = logging.StreamHandler(sys.stdout)  # StreamHandler logs to console
    ch.setLevel(console_level)
    ch_format = logging.Formatter(
        "%(asctime)s $ %(message)s $({})".format(function_name)
    )
    ch.setFormatter(ch_format)
    logger.addHandler(ch)

    logger.propagate = False
    log_dir = Path(get_project_root_dir()) / "logs"
    log_dir.mkdir(parents=True, exist_ok=True)
    log_file = f"{str(log_dir)}/log.log"
    fh = logging.FileHandler(str(log_file))
    fh.setLevel(file_level)
    fh_format = logging.Formatter(
        "%(asctime)s - %(lineno)d - %(levelname)-8s $ %(message)s $ {}".format(
            function_name
        )
    )
    fh.setFormatter(fh_format)
    logger.addHandler(fh)

    return logger

def get_project_root_dir() -> str:
    return str(Path(__file__).parent.parent) # This is your Project Root
