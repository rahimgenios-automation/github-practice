import question3
def filter_user_events(filename, target_user_id):
    for event in question3.stream_events(filename):
        if event["user_id"] == target_user_id:
            yield event
            
for event in filter_user_events("day07/large_user_events.txt", 201):
    print(event)
