# 8-9
def show_messages(texts):
    for text in texts:
        print(text)
texts = ["msg 1", "msg 2", "msg 3"]
show_messages(texts)
print()

# 8-10
def send_messages(old_list, sent_list):
    print(old_list)
    while old_list:
        current = old_list.pop(0)
        print(current)
        sent_list.append(current)
old_messages = ["msg 1", "msg 2", "msg 3"]
sent_messages = []
send_messages(old_messages, sent_messages)
print(old_messages)
print(sent_messages)
print()

# 8-11
def send_messages(old_list, sent_list):
    old_list = old_list[::-1]
    print(old_list)
    while old_list:
        current = old_list.pop()
        print(current)
        sent_list.append(current)
old_messages = ["msg 1", "msg 2", "msg 3"]
sent_messages = []
send_messages(old_messages, sent_messages)
print(old_messages)
print(sent_messages)
print()
