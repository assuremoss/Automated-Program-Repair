"""
Generating data
"""
import argparse
import subprocess
import shutil
import os
import math
from dataclasses import dataclass
import pandas as pd
import tempfile


@dataclass
class APR:
    project_id: str
    bug_id: str
    tool: str

    def worker(self, time_budget: int, patches_dir: str = None) -> str:
        """TODO: Docstring for running.
        Running the tool on the bug within a specific time budget
        :time_budget: Time to repair a bug in minutes 
        :returns: Path to the result file containg plausible patch
        """
        result_path = "/tmp/results:/results"
        if os.path.exists(result_path):
            shutil.rmtree(result_path)
        command = ["docker", "run", "-it", "--rm",
            "-v", result_path, "tdurieux/astor",
            "-i", self.bug_id, 
            "--parameters", 
            "maxtime:" + str(time_budget) + 
            ":" + "stopfirst:true" + ":saveall:false"+
            ":mode:" + str(repair_tool),
        ]

        subprocess.run(command)
        return result_path

    def repair(self):
        """
        :project_id: Project ID
        :repair_too: automated software repair tools jgenprog, jkali,...
        :timeout: User-defined timeout
        :returns: TODO

        """
        data_frame = pd.read_excel(excel_file)
        for _, row in data_frame.iterrows():
            if row["PID"] == project_id:
                timeout = math.ceil(trial * ((row["CT"] + row["TT"]) / 60))
                bug_id = str(row["PID"]) + "-" + str(row["BID"])
                result_path = running(bug_id, repair_tool, timeout)
        result_path = os.path.join(
            os.getenv("DATA_INTERIM_DIR"), project_id + "_" + repair_tool, str(trial) + "T"
        )
        if os.path.exists(result_path):
            shutil.rmtree(result_path)
        src_dir = os.path.join(os.sep, "tmp", "results", "Defects4J")
        shutil.copytree(src_dir, result_path)
        shutil.rmtree(src_dir)

def argument_processing():
    """TODO: Docstring for argment_processing.
      :returns: list of arguments

      """
    parser = argparse.ArgumentParser(
        description="""Running an APR tool with
                 specific time out"""
    )
    parser.add_argument("-t", "--repair_tool", help="Repair tool", required=True)
    parser.add_argument("-p", "--project_id", help="Project ID", required=True)
    parser.add_argument("-e", "--excel", help="Excel file of bugs", required=True)
    args = parser.parse_args()
    return args





def main():
    """TODO: Docstring for main.
    Main function
    :returns: TODO

    """
    args = argument_processing()
    timeout_indexes = [
        int(os.getenv("INTERVAL")) * (2**i) for i in range(1, 2)
    ]

    for timeout in timeout_indexes:
        running_with_timeout(args.excel, args.project_id, args.repair_tool, timeout)


if __name__ == "__main__":
    main()

