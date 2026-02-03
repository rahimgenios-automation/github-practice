import json
events = []
with open("day06/user_events.txt", "r") as f:
    for line in f:
        line = line.strip()
        parts = line.split(",")
        event_dict = {}
        for part in parts:
            key, value = part.split("=")
            if key == "user_id":
                value = int(value)
            event_dict[key] = value
        events.append(event_dict)

with open("day06/events.json", "w") as f:
    json.dump(events, f, indent=4)