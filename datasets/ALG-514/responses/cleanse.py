
import json
from pathlib import Path

input_file_path = 'hwelsters__gpt-3.5-turbo__v001(step-by-step).json'
output_file_path = 'output/' + input_file_path


def __append_to_file(output_file_path: str, data):
    with open(output_file_path, 'a') as outfile:
        outfile.write(json.dumps(data))
        outfile.write("\n")
        outfile.close()
if Path(input_file_path).is_file():
    with open(input_file_path) as f:
        check_set = set()
        for line in f:
            line = json.loads(line)
            if (line['question_number'] in check_set): continue

            with open(output_file_path, 'a') as outfile:
                outfile.write(json.dumps(line))
                outfile.write("\n")
                outfile.close()
            
            check_set.add(line["question_number"])

