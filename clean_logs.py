import json
import re
import sys

def clean_logs(log_file_path):
    with open(log_file_path, 'r') as f:
        log_content = f.read()

    # Regex to find the JSON content after 'Request received by LiteLLM:'
    # This is a bit complex due to the nature of the log file, but it should work.
    # It looks for the start of the JSON object and then finds the matching closing brace.
    json_objects = []
    for match in re.finditer(r'Request received by LiteLLM:\n{\n', log_content):
        start_index = match.end() - 1
        brace_count = 1
        end_index = -1
        for i in range(start_index + 1, len(log_content)):
            if log_content[i] == '{':
                brace_count += 1
            elif log_content[i] == '}':
                brace_count -= 1
            if brace_count == 0:
                end_index = i + 1
                break
        if end_index != -1:
            json_str = log_content[start_index:end_index]
            try:
                json_objects.append(json.loads(json_str))
            except json.JSONDecodeError:
                # Handle cases where the JSON is not perfectly formed
                pass

    prompts = [obj['messages'] for obj in json_objects if 'messages' in obj]

    # The output file will have the same name as the input file, but with "_prompts" added.
    output_file_path = log_file_path.replace('.json', '_prompts.json')

    with open(output_file_path, 'w') as f:
        json.dump(prompts, f, indent=4)

    print(f"Cleaned prompts saved to {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        clean_logs(sys.argv[1])
    else:
        print("Please provide the path to the log file.")
