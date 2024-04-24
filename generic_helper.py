# Author: Dhaval Patel. Codebasics YouTube Channel

import re

def get_str_from_food_dict(food_dict: dict):
    result = ", ".join([f"{int(value)} {key}" for key, value in food_dict.items()])
    return result


def extract_session_id(session_str: str):
    match = re.search(r"/sessions/(.*?)/contexts/", session_str)
    if match:
        extracted_string = match.group(1)
        return extracted_string

    return ""
if __name__=="__main__":
    print(get_str_from_food_dict({"samosa":2,"Chhole":1}))
    # print(extract_session_id("projects/chatbot-for-fooddelivery-i9e9/agent/sessions/18c0f31b-f02f-6c8d-1e3d-364a76f4b3d2/contexts/ongoing-order"))