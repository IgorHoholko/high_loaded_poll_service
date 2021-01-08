
from typing import List, Dict, Tuple
import json
import time
import requests
import os
import json
from pathlib import Path
from collections import Counter
import addict

from util import parseUserAnswers, updateAnalyzerDict, visualize

URL_DATA_DISTRIBUTOR = 'http://host.docker.internal:6060'
DATA_FOLDER_PATH = Path('data')
DATA_ANALYZER_PATH = DATA_FOLDER_PATH / "analyze.json"
ANALYZE_PATH = DATA_FOLDER_PATH / "analyze.jpg"

SLEEP_TIME = 10 # sec


data_template = {
    "last_id_processed": -1,
    "questions" : {},
    "language_codes" : {}
}

def main():
    if not os.path.exists(DATA_FOLDER_PATH):
        os.mkdir(DATA_FOLDER_PATH)

    if os.path.exists(DATA_ANALYZER_PATH):
        with open(DATA_ANALYZER_PATH, 'r') as f:
            data_analyzer = json.load(f)
    else:
        data_analyzer = data_template

    data_analyzer = addict.Dict(data_analyzer)

    while True:
        last_id_processed = data_analyzer['last_id_processed']
        user_answers = requests.get(f"{URL_DATA_DISTRIBUTOR}/user_answers/{last_id_processed}").json()

        print(user_answers)
        if len(user_answers):
            new_data_analyzer = parseUserAnswers(user_answers, URL_DATA_DISTRIBUTOR)
            data_analyzer = updateAnalyzerDict(data_analyzer, new_data_analyzer)

            visualize(data_analyzer, ANALYZE_PATH)

            with open(DATA_ANALYZER_PATH, 'w') as f:
                json.dump(data_analyzer, f)

        time.sleep(SLEEP_TIME)


if __name__ == '__main__':
    main()