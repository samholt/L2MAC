from summarizer_and_modifier import load_code_files_into_dict, count_total_characters, count_key_characters, extract_file_names, format_files_into_prompt_format, embed_all_code_files, cache_or_compute, remove_line_numbers
import numpy as np

# path = './repos/flaskbb' #31K
# path = './repos/flaskSaaS' #1K
# path = './repos/microblog' #2.2K
# path = './repos/flaskex' #595
# path = './repos/flask_jsondash' #27K
# path = './repos/psdash' #4K
# path = './repos/querybook' #71K
path = './repos/solara' #47K








# path = './repos/app' #539K
# path = './repos/timesketch' #69K
# path = './repos/ActorCloud' #52K

# path = "/home/sam/code/DecentralizedGPTsCode/repos/skylines" #32K

# path = './repos/busy-beaver' #12K
# path = './repos/airflow' #812K




# path = './repos/redash' #60K
# path = "/home/sam/code/DecentralizedGPTsCode/repos/quokka" #60K
# path = "/home/sam/code/DecentralizedGPTsCode/repos/indico" #222,257 LOCs
# path = "/home/sam/code/DecentralizedGPTsCode/repos/securedrop" #100,000 LOCs


# path = "/home/sam/code/DecentralizedGPTsCode/repos/PythonBuddy"
# path = '/home/sam/code/DecentralizedGPTsCode/repos/chatbot-ui'
# path = '/home/sam/code/DecentralizedGPTsCode/repos/soMedia'
file_dict = load_code_files_into_dict(path, number_lines=False)
locs_total = np.sum([len(lines) for lines in file_dict.values()])
print(f"Total LOCs: {locs_total}")
print('')
