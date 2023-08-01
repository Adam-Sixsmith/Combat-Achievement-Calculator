
easy_tasks = int(input("How many easy tasks have you done? "))

med_tasks = int(input("How many medium tasks have you done? "))

hard_tasks = int(input("How many hard tasks have you done? "))

elite_tasks = int(input("How many elite tasks have you done? "))

master_tasks = int(input("How many master tasks have you done? "))

grandmaster_tasks = int(input("How many grand maaster tasks have you done? "))

easy_points = easy_tasks 
med_points = med_tasks * 2
hard_points = hard_tasks * 3
elite_points = elite_tasks * 4
master_points = master_tasks * 5
grandmaster_points = grandmaster_tasks * 6

total_points = easy_points + med_points + hard_points + elite_points + master_points + grandmaster_points

points_until_next = None

print("You have a total of ", total_points)

def combat_tier():
    global tier_class
    
    if total_points < 115:
        tier_class = "easy"
        print("You are at the Easy Tier")
    elif total_points < 304 and total_points >= 115:
        tier_class = "med"
        print("You are at the Medium Tier")
    elif total_points < 820 and total_points >= 304:
        tier_class = "hard"
        print("You are at the Hard Tier")
    elif total_points < 1465 and total_points >= 820:
        tier_class = "elite"
        print("You are at the Elite Tier")
    elif total_points < 2005 and total_points >= 1465:
        tier_class = "master"
        print("You are at the Master Tier")
    elif total_points >= 2005:
        tier_class = "grandmaster"
        print("You are at the Grandmaster Tier")
        
def next_tier():
    
    if tier_class == "easy":
        points_until_next = 115 - total_points
        print("You need",points_until_next, "points until the next tier.")
    elif tier_class == "med":
        points_until_next = 304 - total_points
        print("You need",points_until_next, "points until the next tier.")
    elif tier_class == "hard":
        points_until_next = 820 - total_points
        print("You need",points_until_next, "points until the next tier.")
    elif tier_class == "elite":
        points_until_next = 1465 - total_points
        print("You need",points_until_next, "points until the next tier.")
    elif tier_class == "master":
        points_until_next = 2005 - total_points
        print("You need",points_until_next, "points until the next tier.")
    elif tier_class == "grandmaster":
        print("You're already a Grandmaster.....")

        
combat_tier()

next_tier()