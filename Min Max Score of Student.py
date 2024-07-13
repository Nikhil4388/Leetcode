class Score:
    def highScore(self, student_scores):
        sum_score = {}

        # Step 1: Calculate total and count for each student
        for name, score in student_scores:
            score = int(score)
            if name in sum_score:
                sum_score[name]["total"] += score
                sum_score[name]["count"] += 1
            else:
                sum_score[name] = {'total': score, "count": 1}

            # Step 2: Sort items by average score and then by name
        sorted_items = sorted(sum_score.items(), key=lambda item: (item[1]['total'] / item[1]['count'], item[0]))
        
        # Debug print for sorted items
        print("sorted_items------->", sorted_items)

        # Calculate max average
        max_avg = sorted_items[-1][1]['total'] / sorted_items[-1][1]['count']
        
        # Calculate min average
        min_avg = sorted_items[0][1]['total'] / sorted_items[0][1]['count']

        return max_avg, min_avg

# Input data
student_scores = [
    ["Alice", "85"],
    ["Bob", "90"],
    ["Alice", "95"],
    ["Bob", "80"],
    ["Charlie", "70"]
]

# Create an instance of the Score class
score = Score()

# Calculate and print the highest and lowest average scores
max_avg, min_avg = score.highScore(student_scores)
print("Highest Average Score:", max_avg)
print("Minimum Average Score:", min_avg)
