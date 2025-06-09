speed_log = [30, 25, 65, 80]
speed_limit = 50
violations = []
for speed in speed_log:
    if speed > speed_limit:
        violations.append(speed)
print("Number of violations:", len(violations))
print("Vehicles exceeding speed limit:", violations)
