
import re
from rake_nltk import Rake

def extract_keywords_rake(text, top_n=10):
    r = Rake()
    r.extract_keywords_from_text(text)
    return [kw for kw in r.get_ranked_phrases()[:top_n]]

def clean_job_description(text):
    text = text.strip().lower()
    text = re.sub(r'\s+', ' ', text)
    return text

# ### TEST
# if __name__ == "__main__":
#     jd = "We need a Backend Developer skilled in Django, REST APIs, and PostgreSQL."
#     jd = clean_job_description(jd)
#     print(extract_keywords_rake(jd, top_n=5))
