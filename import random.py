import random
import csv


players_names = ['Anna', 'Ben', 'Ken', 'Barbi', 'Piter']
player_score = []
for i in players_names:
#    total_score = 0
    for j in range(100):
        score = random.randint(0, 1000)
#        total_score += score
        player_score.append((i, score))
print(player_score)


with open ('game.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player name', 'Score'])
    writer.writerows(player_score)


#4
with open ('game.csv', 'r') as input_file, open('high_scores.csv', 'w', newline='') as output_file:
    reader = csv.DictReader(input_file)
    player_high_score = {}
    for row in reader:
    #    print(row)
        name = row['Player name']
        score = row['Score']
        print(name, score)
        if not name in player_high_score.keys():
            player_high_score[name] = score
        else:
            if player_high_score[name] < score:
                player_high_score[name] = score


    print(player_high_score)


    writer = csv.writer(output_file)
    writer.writerow(['Player name', 'Score'])
    for name, score in player_high_score.items():
        writer.writerow([name, score])
 
            






    





