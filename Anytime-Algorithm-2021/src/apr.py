"""
This module contains a function to run the repair process within time budget
"""
from dataclasses import dataclass
import logging
import os
from pathlib import Path
import subprocess
import tempfile
from time import gmtime
from time import strftime

from .utils import function_logger


@dataclass
class APR:
    benchmark: str
    bug_id: str
    tool: str
    seed: int = 10 # For reproducibility, feel free to change it

    def start(self, time_budget: int, patches_dir: str = None) -> str:
        """TODO: Docstring for running.
        Running the tool on the bug within a specific time budget
        :time_budget: Time to repair a bug in minutes 
        :returns: Path to the result file containg plausible patch
        """
        logger = function_logger(file_level=logging.INFO, console_level=logging.DEBUG)
        # the result will be stored in a tempopary dir if users do not specify
        if patches_dir is None:
            patches_dir = tempfile.gettempdir()

        # Use container name as an identifier to kill the repair process
        container_name = f"{time_budget}_{self.tool}_{self.benchmark}_{self.bug_id}_{self.seed}"

        # Patch will be saved based on time of executing the repair process
        current_date = strftime("%Y-%m-%d-%H-%M-%S", gmtime())
        result_dir = "{0}/{1}/{2}:/results".format(str(Path(patches_dir) / 'results'), current_date, str(time_budget))
        command= (['docker', 'run', '-it',
                    "--name", container_name,
                    "--rm", '-v', result_dir,
                    'tdurieux/repairthemall', str(self.tool),
                    '-b', str(self.benchmark) ,
                    '-i', str(self.bug_id),
                    '--seed', str(self.seed)])

        process = subprocess.Popen(command)

        logger.info("Repairing {} ".format(container_name))
        try:
            outs, errs = process.communicate(timeout=(int(time_budget) * 60))
        except TimeoutExpired:
            logger.info("Repair process terminated")
            os.system("docker kill {}".format(container_name))

        logger.info("Tool: {}, Benchmark: {}, Bug ID: {}, Time budget: {}, Result dir: {}".format(self.tool, self.benchmark, self.bug_id, time_budget, result_dir))


