import os

# Part 1
left_locations_ids = []
right_locations_ids = []

#input = open("input_example.txt", "r")
input = open("input.txt", "r")

for line in input:
    left = line.split("   ")[0]
    right = line.split("   ")[1]
    
    left_locations_ids.append(int(left))
    right_locations_ids.append(int(right))

left_locations_ids.sort()
right_locations_ids.sort()

distances = []

for left_id, right_id in zip(left_locations_ids, right_locations_ids):
    distances.append(abs(left_id - right_id))

print(sum(distances))


# Part 2
occurrences_tuples = []

for id in left_locations_ids:
    occurrences_tuples.append([id, 0])

for tuple in occurrences_tuples:
    for id in right_locations_ids:
        if tuple[0] == id:
            tuple[1] += 1

similarity_scores = []

for tuple in occurrences_tuples:
    similarity_scores.append(tuple[0] * tuple[1])

#print(occurrences_tuples)
#print(similarity_scores)
print(sum(similarity_scores))
