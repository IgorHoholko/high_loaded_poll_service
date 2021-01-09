
from typing import List, Dict, Tuple
import requests
from collections import Counter
import seaborn as sbn
import matplotlib.pyplot as plt



def parseUserAnswers(user_answers: List[Dict], URL: str) -> Dict:
    """
    :param user_answers: [{id: int, answer_id: int, user_id: int}, ...]
    :return:
    """
    questions_dict = {}
    language_codes_dict = {}

    cache = {}
    for user_answer in user_answers:
        answer_id = user_answer['answer_id']
        user_id = user_answer['user_id']
        id = user_answer['id']

        # answer parsing
        answer_cache_key = f"answer_id{answer_id}"
        if answer_cache_key in cache.keys():
            answer = cache[answer_cache_key]
        else:
            answer = requests.get(f"{URL}/answers/{answer_id}").json()[0]
            cache[answer_cache_key] = answer

        question_id = answer['question_id']
        answer_text = answer['text']

        #question parsing
        question_cache_key = f"question_id{question_id}"
        if question_cache_key in cache.keys():
            question = cache[question_cache_key]
        else:
            question = requests.get(f"{URL}/questions/{question_id}").json()[0]
            cache[question_cache_key] = question
        question_text = question['text']

        # user_parsing
        user_cache_id = f"user_id{user_id}"
        if user_cache_id in cache.keys():
            user = cache[user_cache_id]
        else:
            user = requests.get(f"{URL}/users/{user_id}").json()[0]
            cache[user_cache_id] = user

        lan_code = user['language_code']


        # Forming return
        if question_id not in questions_dict.keys():
            questions_dict[question_id] = {
                "text" : question_text,
                "answers" : Counter()
            }
        questions_dict[question_id]['answers'][answer_text] += 1

        if question_id not in language_codes_dict.keys():
            language_codes_dict[question_id] = {
                "codes" : Counter()
            }
        language_codes_dict[question_id]['codes'][lan_code] += 1

    new_data_analyzer = {
        "last_id_processed": id,
        "questions" : questions_dict,
        "language_codes" : language_codes_dict
    }


    return new_data_analyzer


def updateAnalyzerDict(adict: Dict, new_adict: Dict) -> Dict:

    print(adict)
    print(new_adict)

    for question_id in new_adict['questions'].keys():
        for answer, count in new_adict['questions'][question_id]['answers'].items():
            adict['questions'][question_id]['answers'][answer] += count
            adict['questions'][question_id]['text'] = new_adict['questions'][question_id]['text']

    for question_id in new_adict['questions'].keys():
        for code, count in new_adict['language_codes'][question_id]['codes'].items():
            adict['language_codes'][question_id]['codes'][code] += count

    adict['last_id_processed'] = new_adict['last_id_processed']

    return adict

# "language_codes": {"1": {"codes": {"ru": 39, "en": 3}}}}
def visualize(adict: Dict, save_path: str):

    questions = list(adict['questions'].values())
    question_text = questions[0]['text']
    answers = questions[0]['answers']

    lan_codes = adict['language_codes'][1]['codes']

    ans_vals = list(answers.values())
    ans_names = list(answers.keys())

    lan_vals = list(lan_codes.values())
    lan_names = list(lan_codes.keys())
    print(lan_vals, lan_names)

    fig, axs = plt.subplots(1, 2, figsize=(14, 6), constrained_layout=True, )

    # Set dark grid
    sbn.set()

    fig.suptitle(question_text, size=25, )

    ax1 = sbn.barplot(ans_names, ans_vals, palette='Greens_r', ax=axs[0], )
    for item in ax1.get_xticklabels():
        item.set_rotation(30)
        item.set_fontsize(16)

    axs[1].pie(x=lan_vals, autopct="%.1f%%", explode=[0.05] * len(lan_names), labels=lan_names,
               pctdistance=0.5, textprops={'fontsize': 14})

    # Save figure
    plt.savefig(save_path, dpi=1000)

    plt.cla()
    plt.clf()
    plt.close()
