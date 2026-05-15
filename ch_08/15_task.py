# TASK

# SYRVEY PIPELINE
# SURVEY ANALYSIS TOOL

# functions:
#
# 1. record_response(respondent, *answers, source="direct", **metadata)
# stores single response
# return dictionary
#
# 2. summarize_responses(responses, metric="...", exclude=None)
#! default arguments are evaluated only once 
#! at the time the function is defined
# metric parameter controls output:
# metric="count" - return total number of responses
# metric="sources" - return list of unique sources
# metric="answers_flat" - list of all answers
# 
# 3. apply_filter(responses, *keywords, case_sensitive=False)
# returns a filtered copy of responses 
# (when at least one answer contains keywords)
#
# 4. generate_report(responses, title="Survey Report", **options)
# print report
# options can include:
# show_metadata=True/False
# max_responses=N
#
# 5. run_pipeline(raw_data, *filter_keywords, report_title="Results", **report_options)
#



def record_response(respondent, *answers, source="direct", **metadata):
    response = {}
    response["respondent"] = respondent
    response["answers"] = list(answers)
    response["source"] = source
    response["metadata"] = metadata
    return response

def summarize_responses(responses, metric="count", exclude=None):
    if exclude is None:
        exclude = []
    filtered = [r for r in responses if r["respondent"] not in exclude]
    if metric == "count":
        return len(filtered)
    if metric == "sources":
        return list(set(f["source"] for f in filtered))
    if metric == "answers_flat":
        return [a for f in filtered for a in f["answers"]]

def apply_filter(responses, *keywords, case_sensitive=False):
    if case_sensitive:
        return [r for r in responses if any(a in keywords for a in r["answers"])]
    else:
        lower_keywords = [k.lower() for k in keywords]
        return [r for r in responses if any(a.lower() in lower_keywords for a in r["answers"])]

def generate_report(responses, title="Survey Report", **options):
    show_metadata = options.get("show_metadata", False)
    max_responses = options.get("max_responses", len(responses))
    print(f"=== {title} ===")
    print(f"Total responses: {len(responses)}")
    print()
    m = 0
    for r in responses:
        m += 1
        print(f"{m}. {r['respondent']} | source: {r['source']}")
        print(f"Answers: {r['answers']}")
        if show_metadata:
            print(f"Metadata: {r['metadata']}")
        if m == max_responses:
            break

def run_pipeline(raw_data, *filtered_keywords, report_title="Results", **report_options):
    filtered_list = apply_filter(raw_data, *filtered_keywords)
    count = summarize_responses(filtered_list)
    generate_report(filtered_list, title=report_title, **report_options)
    return (filtered_list, count)



r0 = record_response("0", "no", "no", "no")
r1 = record_response("Alpha", "no", "no", "yes", source="web", a1="a1")
r2 = record_response("Bravo", "no", "yes", "no", source="email", b1="b1")
r3 = record_response("Charlie", "no", "yes", "yes", source="direct", c1="c1")
r4 = record_response("Delta", "yes", "no", "no", source="web", d1="d1", d2="d2")
r5 = record_response("Echo", "yes", "no", "yes", source="email", e1="e1", e2="e2")
r6 = record_response("Foxtrot", "yes", "yes", "no", source="web", f1="f1", f2="f2")
r7 = record_response("Golf", "yes", "yes", "yes", source="web", g1="g1", g2="g2", g3="g3")
r8 = record_response("Hotel", "yes", "no", "no", "no", source="web", h1="h1", h2="h2", h3="h3")

responses = [r0, r1, r2, r3, r4, r5, r6, r7, r8]
print(responses)
print()

"""
summarize = summarize_responses(responses)
print(summarize)
summarize = summarize_responses(responses, metric="sources")
print(summarize)
summarize = summarize_responses(responses, metric="answers_flat")
print(summarize)

filtered = apply_filter(responses, "yes")
print(filtered)
print()

generate_report(responses)
print()
generate_report(responses, max_responses=3)
print()
generate_report(responses, show_metadata=True)
print()
generate_report(responses, title="Results", max_responses=3, show_metadata=True)
print()
"""

filtered_list, count = run_pipeline(responses, "yes", report_title="'Yes' responses", show_metadata=True, max_responses=5)
print(f"\nPipeline returned {count} matching responses.")
print()
print(filtered_list)
print()