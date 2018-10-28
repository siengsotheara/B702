import os
import sys
import logging

current_dir = os.path.dirname(os.path.realpath(__file__))
target_dir = os.path.sep.join(current_dir.split(os.path.sep)[:-2])
sys.path.insert(0,target_dir)

import pandas
import argparse
import dialogflow_v2 as dialogflow
from config import DIALOGFLOW_PROJECT_ID

def create_intent(display_name, training_phrases_parts, message_texts):
    """Create an intent of the given intent type."""
    try:
        intents_client = dialogflow.IntentsClient()

        parent = intents_client.project_agent_path(DIALOGFLOW_PROJECT_ID)
        training_phrases = []
        for training_phrases_part in training_phrases_parts:
            part = dialogflow.types.Intent.TrainingPhrase.Part(
                text=training_phrases_part)

            # Here we create a new training phrase for each provided part.
            training_phrase = dialogflow.types.Intent.TrainingPhrase(parts=[part])
            training_phrases.append(training_phrase)

        text = dialogflow.types.Intent.Message.Text(text=message_texts)
        message = dialogflow.types.Intent.Message(text=text)

        intent = dialogflow.types.Intent(
            display_name=display_name,
            training_phrases=training_phrases,
            messages=[message])

        response = intents_client.create_intent(parent, intent)

        print('Intent created: {}'.format(response))
    except Exception as e:
        print e

if __name__ == '__main__':
    logging.info('start')
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'bankingbot-48180-0408b9abf98a.json'
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('--file', help='File path. Required.', required=True)
    args = parser.parse_args()
    pandas.options.mode.use_inf_as_na = ""

    try:
        xlsx = pandas.ExcelFile(args.file)

        df = xlsx.parse('DATA')
        df.columns = ['A','B','C']

        for phrase, rsp in df.groupby('A'):
            print phrase,rsp.B.values.tolist(),rsp.C.values.tolist()
            create_intent(phrase, rsp.B.values.tolist(), rsp.C.values.tolist())
    except Exception as e:
        raise e