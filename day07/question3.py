def stream_events(filename):
    with open(filename, "r") as f:
        for lines in f:
            lines = lines.strip()
            parts = lines.split(",")
            part_dict = {}
            for part in parts:
                key, value = part.split("=")
                if key == "user_id":
                    value  = int(value)
                part_dict[key] = value
            yield part_dict






