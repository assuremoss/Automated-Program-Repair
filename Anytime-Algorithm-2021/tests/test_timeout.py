from ..src.apr import APR

def test_jGenProg_1_minute():
    apr = APR(benchmark="Defects4J", bug_id="5", tool="jGenPRog")
    apr.start()

