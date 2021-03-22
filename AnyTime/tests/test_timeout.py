import time

from src.apr import APR
def test_jGenProg_1_minute():
    apr = APR(benchmark="Defects4J", bug_id="Chart-5", tool="jGenProg")
    start = time.time()
    apr.start(1)
    end = time.time()
    elapsed = end - start
    # Some seconds delay as time for setting up repairing process
    assert 60 <= elapsed <= 70


