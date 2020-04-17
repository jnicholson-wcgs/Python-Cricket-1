# WCGS Cricket Program
#
# Task One
#
# over() - an over is cricket is 6 balls bowled by the batting team
#
# Write a subroutine called over() which 
# Takes 1 parameter:
#      Parameter 1: the number of the over
# Returns:
#     The total number of runs scored
#
# The routine should:
#    - Print out the over number paramter passed in, for example:
#         Over number: 2 
#    - Prompt the user to enter the scores for each ball in the over, for example:
#         Please enter the score for ball 1: 
#    - Keep a running total the number of runs scored in the over 
#
# Define your function below


def over (over_number) :
  return 0

over (1)

# Task Two
#
# Write a test plan with at least three tests that can be performed on your over() routine
# Include your test plan below:
# 
# For, example:
# Test 1: Call over with a negative over number
# If your test crashes your program, comment it out after running it

over (-1)


# Task Three
# Innings. An innings in cricket a number of overs bowled to a team. In limited overs, the bowling team
# bowls a limited/set number of overs, e.g. 20 overs or 50 overs.
#
# Write a routine called innings() which:
# Takes 2 parameters:
#      Parameter 1: team_name - the name of the team that is playing
#      Parameter 1: novers - the number of overs to be bowled in the innings
#
# Returns: 
#      The total number of runs scored by the team in the innings
#
# The routine should call the routine over() for each over in the innings
# For example, innings ("WCGS", 3) will return the number of runs scored by WCGS in their 3 over innings
#
# Define your function below

def innings (team_name, novers) :
  return 0

innings ("WCGS", 1)

# Task Four
#
# Write a test plan with at least three tests that can be performed on your innings() routine
# For, example:
# Test 1: Call innings()  with a negative over number
# If your test crashes your program, comment it out after running it

innings ("Wilsons", -1)


# Task Five
# Match. A cricket match consists of two teams having the same number of innings and 
# deciding which team has scored the most runs.
#
# Write a routine call match() which:
#
# Takes no arguments
#
# Returns no value
#
# The routine should
#        Prompt the user for the opposition team name
#        Prompt the user for the number of innings
#        Prompt the user for the number of overs per innings
#        "Toss a coin" (heads or tails) to determine which team bats first.
#        Play out the match for correct number of innings and overs
#        Declare the winning team

# Define your function below

def match () :
  print ("Thanks for comming")

match()

# Task Six
# Highlight three places in your match() routine where you do validation
# Validation 1:
# Validation 2:
# Validation 3:
#
# Hightlight other validations you have done on in your code
# Validation 4:
# Validation 5:

#
# Task Seven
#
# Add "try and except" handling to your over() routine to ensure that only integer values are added
# Show below the values you used for testing exception handling
#

