frames = []

with open(r"Dataset\bambi_downloads\146_gt.txt") as f:
    for line in f:
        parts = line.strip().split(",")

        track_id = parts[1]

        if track_id == "2555":
            frames.append(int(parts[0]))

print("Frames:")
print(frames)
print("Total:", len(frames))

selected = {1893, 1973, 2073, 2153, 2213}

with open(r"Dataset\bambi_downloads\146_gt.txt") as f:
    for line in f:
        parts = line.strip().split(",")
        if parts[1] == "2555" and int(parts[0]) in selected:
            print(line.strip())