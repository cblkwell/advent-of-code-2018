import sys
from collections import deque

players, marbles = int(sys.argv[1]), int(sys.argv[2])

# This is just a method to describe the current state of the game.
def describe_game(circle, scores, played_marble):
    print(f'After playing marble {played_marble}:')
    print('-------------------------------------')
    # print(circle)
    print("The current marble is:")
    print(circle[0])
    print("Current scores are:")
    print(scores)
    print(f"The high score is {max(scores.values())}.")


# This is the function which does a normal marble placement, putting
# a marble two slots clockwise. We take three inputs; the current state
# of the circle, the current marble, and the new marble we're adding.
def normal_placement(circle, new_marble):

    # If placement is normal, this should be straightforward; thanks
    # to using a deque, we don't need to do a bunch of logic to
    # figure out where we are in the queue. We can just rotate and
    # append, easy peasy.
    circle.rotate(-2)
    circle.appendleft(new_marble)
    
    return circle


# This is a function which handles point-scoring placement. Here, we
# don't need the new marble because it's not going to be used (except
# to calculate points, and we do that in the play_marble function.
def scoring_placement(circle):

    # Using deque, we can simplify a ton of this logic. We rotate
    # the deque seven steps "counterclockwise" and then pop off the
    # last value.
    circle.rotate(7)
    bonus_score = circle.popleft()

    return circle, bonus_score


# We need a function to play a marble; the inputs are the circle,
# the current marble, and the new marble.
def play_marble(circle, new_marble):
    # Score is zero for this play to start with.
    score = 0

    # If the marble is divisible by 23, this is a scoring
    # placement.
    if new_marble % 23 == 0:
        circle, bonus_score = scoring_placement(circle)
        score = new_marble + bonus_score
    # If not, then this isn't a scoring placement, so score will remain
    # zero.
    else:
        circle = normal_placement(circle, new_marble)

    return circle, score


# GAME BEGINS HERE

# So, part two makes using a simple list pretty untenable (it runs
# ~forever~). Thanks to github.com/mosephine I learned about the
# deque class from the collections library, which works similarly
# but is much more efficient for what we want to do. We can also say
# that the current marble will always be at the "start" of the circle,
# so we don't need to keep track of it anymore.
circle = deque([0])
# We also nsomething to keep track of scores; a dict will work.
scores = {}
# We'll also need something to keep track of the current player.
player = 1
# There also needs to be a variable to keep track of the currently
# *played* marble, which is different from the current marble.
playing_marble = 1

# The game starts with the "zeroth" marble already played, since this
# needs to be done regardless of how many marbles or players there are.
while playing_marble <= marbles:

    # So, we play the playing_marble and get back a new game state and
    # the score of the play.
    circle, score = play_marble(circle, playing_marble)
    
    # We need to do some special casing because at first, the scoring
    # dict will be empty and we'll need to populate it. If the player
    # already has a score, then we have the easy case.
    if player in scores:
        scores[player] += score
    # If the player *doesn't* have a score yet, then we need to establish
    # their score.
    else:
        scores[player] = score

    # describe_game(circle, scores, playing_marble)

    # Now we increment the playing_marble counter.
    playing_marble += 1

    # For players, we need to be a bit more careful; if we are at the
    # last player, the next player will be the first player.
    if player == players:
        player = 1
    # Otherwise, it's just the next player.
    else:
        player += 1

describe_game(circle, scores, playing_marble)
