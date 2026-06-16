# SERIES OF API CALLS

from operator import itemgetter
import requests
import plotly.express as px

# Make an API call and check the response.
url = "https://hacker-news.firebaseio.com/v0/topstories.json"
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a new API call for each submission
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id} status: {r.status_code}")
    response_dict = r.json()
    
    # Build a dictionary for each article.
    submission_dict = {
        "title": response_dict["title"],
        "hn_link": f"https://news.ycombinator.com/item?id={submission_id}",
        "comments": response_dict["descendants"],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter("comments"), reverse=True)

'''
for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
'''

subms, comms = [], []
for submission_dict in submission_dicts:
    subm_name = submission_dict['title']
    subm_link = submission_dict['hn_link']
    subm_full = f"<a href='{subm_link}'>{subm_name}</a>"
    subms.append(subm_full)
    comms.append(submission_dict['comments'])

# Make visualization.
title = "Most Active Discussions on Hacker News"
labels = {"x": "Submission", "y": "Comments"}
fig = px.bar(
    x=subms, y=comms, 
    title=title, labels=labels,
)
fig.update_layout(
    title_font_size=28, 
    xaxis_title_font_size=20,
    yaxis_title_font_size=20
)
fig.update_traces(
    marker_color="SteelBlue", marker_opacity=0.6
)
fig.show()
