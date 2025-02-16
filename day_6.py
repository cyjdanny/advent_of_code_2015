import pandas as pd
grid = pd.DataFrame(False, index=range(1000), columns=range(1000), dtype=bool)

with open('input/day6.txt ', 'r') as file_object:
    instructions = file_object.read().strip().splitlines()

#part 1
for instruction in instructions:
    parts = instruction.split(" ")

    if parts[0] == "turn":
        action = parts[1]
        start = parts[2]
        end = parts[4]
    elif parts[0] == "toggle":
        action = "toggle"
        start = parts[1]
        end = parts[3]

    x1, y1 = map(int, start.split(","))
    x2, y2 = map(int, end.split(","))

    if action == "on":
        grid.loc[x1:x2, y1:y2] = True
    elif action == "off":
        grid.loc[x1:x2, y1:y2] = False
    elif action == "toggle":
        grid.loc[x1:x2, y1:y2] = ~grid.loc[x1:x2, y1:y2]

lights_on = grid.sum().sum()
print(f"how many lights are lit?: {lights_on}")

#part 2
grid = pd.DataFrame(0, index=range(1000), columns=range(1000))

for instruction in instructions:
    parts = instruction.split()

    if parts[0] == "turn":
        action = parts[1]
        start_x, start_y = map(int, parts[2].split(","))
        end_x, end_y = map(int, parts[4].split(","))
    elif parts[0] == "toggle":
        action = "toggle"
        start_x, start_y = map(int, parts[1].split(","))
        end_x, end_y = map(int, parts[3].split(","))

    if action == "on":
        grid.loc[start_x:end_x, start_y:end_y] += 1
    elif action == "off":
        grid.loc[start_x:end_x, start_y:end_y] = grid.loc[start_x:end_x, start_y:end_y].map(
            lambda x: max(0, x - 1))
    elif action == "toggle":
        grid.loc[start_x:end_x, start_y:end_y] += 2

total_brightness = grid.values.sum()
print("Total brightness:", total_brightness)
