def safe_stream_events(filename):
    with open(filename, "r") as f:
        for line in f:
            try:
                line = line.strip()
                parts = line.split(",")
                event = {}
                for part in parts:
                    key, value = part.split("=")
                    event[key] = value
                if "user_id" not in event or "event" not in event or "time" not in event:
                    continue
                try:
                    print(event["user_id"]) = print(int(event["user_id"]))
                except ValueError:
                    continue 
                yield event
            except Exception:
                continue


for event in safe_stream_events("day08/dirty_user_events.txt"):
    print(event)