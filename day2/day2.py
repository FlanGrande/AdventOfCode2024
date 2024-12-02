import os

#input = open("input_example.txt", "r")
input = open("input.txt", "r")

reports = []
safe_reports = 0

for line in input:
    reports.append(list(map(int, line.split(" "))))

for report in reports:
    is_safe = True
    
    if sorted(report) != report and sorted(report, reverse = True) != report:
        is_safe = False
        print("NOT SAFE: Not sorted")
        print(report)
        print()
        continue

    # If it's sorted, then it's potentially safe
    if sorted(report) == report:
        current_level = report[0]
        has_problem_dampener_triggered = False

        for i in range(1, len(report)):
            difference = abs(current_level - report[i])
            
            if difference <= 0 or difference > 3:
                is_safe = False
                print("NOT SAFE: Low to High")
                print(report)
                print()
                break
            else:
                current_level = report[i]
    elif sorted(report, reverse = True) == report:
        current_level = report[0]
        has_problem_dampener_triggered = False

        for i in range(1, len(report)):
            difference = abs(current_level - report[i])

            if difference <= 0 or difference > 3:
                is_safe = False
                print("NOT SAFE: High to Low")
                print(report)
                print()
                break
            else:
                current_level = report[i]
    
    if is_safe:
        print("SAFE:")
        print(report)
        print()
        safe_reports += 1

print(safe_reports)
