# Prompts the user for 9 par values, and stores them in a list
def getHolesPar():
    return [int(input('Please input the par value for a golf hole (Please enter either 3, 4, or 5): ')) for i in range(9)]

# Prompts the user for 9 par values, and stores them in a list
def getPlayerScore():
    return [int(input('Please input how well you did today (scores cannot be negative): ')) for i in range(9)]

def getStats(par, score):
    score_list = []
    for i in range(9):
        score_list.append(par[i] - score[i])

    eagles = score_list.count(2)
    birdies = score_list.count(1)
    pars = score_list.count(0)
    bogey = score_list.count(-1)
    double_bogey = score_list.count(-2)

    stats = (
        eagles, birdies, pars, bogey, double_bogey
    )

    return stats

def beutify_stats(stats):
    beautified_stats = {
        "Eagles" : stats[0],
        "Birdies" : stats[1],
        "Pars"   : stats[2],
        "Bogey"  : stats[3],
        "Double Bogey" : stats[4]
    }

    return beautified_stats

def getCoursePar(par):
    return sum([i for i in par])

def getScore(score):
    return sum([i for i in score])

def display_result(course_par, player_score, stats, total_par, total_score):
    print ("\nThis is how well you did today: \n")
    print ("The course par was: " + str(total_par) + "\n")
    print ("Your total score was: " + str(total_score) + "\n")
    print ("You got " + str(stats["Eagles"]) + " Eagles, " + str(stats['Birdies']) + " Birdies, " +
           str(stats["Pars"]) + " Pars, " + str(stats["Bogey"]) + " Bogies, and " + str(stats["Double Bogey"]) +
           " Double Bogies.\n"
    )
    print ("Better luck next time!")



print ('Welcome to stat calculator, we hope you did well today!')

course_pars = getHolesPar()
player_scores = getPlayerScore()
stats = getStats(course_pars, player_scores)
player_stats = beutify_stats(stats)
total_par = getCoursePar(course_pars)
total_score = getScore(player_scores)


display_result(course_pars, player_scores, player_stats, total_par, total_score)
