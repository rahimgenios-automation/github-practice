def safe_stream_events(filename):
    with open(filename, "r") as f:
        for line in f:
            stats["Total"] += 1
            try:
                line = line.strip()
                parts = line.split(",")
                event = {}
                for part in parts:
                    key, value = part.split("=")
                    event[key] = value
                if "user_id" not in event or "event" not in event or "time" not in event:
                    stats["Invalid"] += 1
                    continue
                try:
                    event["user_id"] = int(event["user_id"])
                except ValueError:
                    stats["Invalid"] += 1
                    continue 
                stats["Valid"] += 1
                yield event
            except Exception:
                stats["Invalid"] += 1
                continue


stats = {"Total": 0, "Valid": 0, "Invalid": 0}

for event in safe_stream_events("day08/dirty_user_events.txt"):
    print(event)

print("\nData Quality Report")
print("-------------------")
print("Total lines:", stats["Total"])
print("Valid records:", stats["Valid"])
print("Invalid records:", stats["Invalid"])