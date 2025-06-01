#!/usr/bin/env python
import warnings

from datetime import datetime

from analyst_crew.crew import AnalystCrew

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    try:
        AnalystCrew().crew().kickoff()
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")

if __name__ == "__main__":
    print(f"AnalystCrew started at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    run()
    