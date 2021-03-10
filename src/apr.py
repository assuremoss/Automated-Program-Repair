"""
Generating data
"""
import argparse
import subprocess
import shutil
import os
import math
import pandas as pd

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


def running(bug_id, repair_tool, timeout):
    """TODO: Docstring for running.
    Running the tool on the bug within a specific timeout
    :bug_id: Bug ID follow the pattern: ProjectID_BugID
    :returns: TODO
    """
    result_path = "/tmp/results:/results"
    if os.path.exists(result_path):
        shutil.rmtree(result_path)
    command = [
        "docker",
        "run",
        "-it",
        "--rm",
        "-v",
        result_path,
        "tdurieux/astor",
        "-i",
        bug_id,
        "--parameters",
        "maxtime:"
        + str(timeout)
        + ":"
        + "stopfirst:true"
        + ":saveall:false"
        + ":mode:"
        + str(repair_tool),
    ]

    subprocess.run(command)
    return result_path


def running_with_timeout(excel_file, project_id, repair_tool, trial):
    """TODO: Docstring for running_with_timeout.
    :excel_file: The excel file containing bug data
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

