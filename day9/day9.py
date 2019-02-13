import sys

players, marbles = int(sys.argv[1]), int(sys.argv[2])

# This is just a method to describe the current state of the game.
def describe_game(circle, cur_marble, scores, played_marble):
    print(f'After playing marble {played_marble}, the current state of the game is:')
    print(circle)
    print("The current marble is:")
    print(cur_marble)
    print("Current scores are:")
    print(scores)


# This is the function which does a normal marble placement, putting
# a marble two slots clockwise. We take three inputs; the current state
# of the circle, the current marble, and the new marble we're adding.
def normal_placement(circle, cur_marble, new_marble):
    
    cur_position = circle.index(cur_marble)
    # Let's check to see if this is the easy case, where we're not
    # going to loop over the end of the list. The only time this is
    # the case is where our current position is at the end of the
    # list (if we're one short of that, we just append).
    if cur_position != len(circle) - 1:
        circle.insert((cur_position + 2), new_marble)
    # If we were at the last position in the list, then we insert
    # the new marble at position 1 (because that's "two spaces
    # clockwise" from the end of the list).
    else:
        circle.insert(1, new_marble)

    # Return the new circle, and the new marble, which will become
    # the current marble.
    return circle, new_marble


# This is a function which handles point-scoring placement. Here, we
# don't need the new marble because it's not going to be used (except
# to calculate points, and we do that in the play_marble function.
def scoring_placement(circle, cur_marble):

    cur_position = circle.index(cur_marble)
    # If the current marble's index is less than seven, we just need
    # to work from the end of the list to figure things out.
    if cur_position < 7:
        offset = 7 - cur_position
        cur_marble = circle[len(circle) - offset - 1]
        bonus_score = circle.pop(len(circle) - offset)
        
    # If our current position is exactly seven, we have an annoying
    # special case.
    elif cur_position == 7:
        cur_marble = circle[len(circle) - 1]
        bonus_score = circle.pop(0)
    # If the current marble's index is >= 8, the next
    # step is pretty easy.
    else:
        cur_marble = circle[cur_position - 8]
        bonus_score = circle.pop(cur_position - 7)

    # Now we return the circle, the current marble, and the bonus
    # score from removing the other marble.
    return circle, cur_marble, bonus_score


# We need a function to play a marble; the inputs are the circle,
# the current marble, and the new marble.
def play_marble(circle, cur_marble, new_marble):
    # Score is zero for this play to start with.
    score = 0

    # If the marble is divisible by 23, this is a scoring
    # placement.
    if new_marble % 23 == 0:
        circle, cur_marble, bonus_score = scoring_placement(circle, cur_marble)
        score = new_marble + bonus_score
    # If not, then this isn't a scoring placement, so score will remain
    # zero.
    else:
        circle, cur_marble = normal_placement(circle, cur_marble, new_marble)

    return circle, cur_marble, score


# GAME BEGINS HERE

# Every marble game has a list of the marbles in it. It starts
# empty. I'm tempted to create a new object with methods to
# support a "circular list" but I think this is probably overkill
# at least for part one.
circle = [0]
# We also have a variable to keep track of the current marble.
current_marble = 0
# We also nsomething to keep track of scores; a dict will work.
scores = {}
# We'll also need something to keep track of the current player.
player = 1
# There also needs to be a variable to keep track of the currently
# *played* marble, which is different from the current marble.
playing_marble = 1

# The game starts with the "zeroth" marble already played, since this
# needs to be done regardless of how many marbles or players there are.
while playing_marble =< marbles:

    # So, we play the playing_marble and get back a new game state and
    # the score of the play.
    circle, current_marble, score = play_marble(circle, current_marble, playing_marble)
    
    # We need to do some special casing because at first, the scoring
    # dict will be empty and we'll need to populate it. If the player
    # already has a score, then we have the easy case.
    if scores[player]:
        scores[player] += score
    # If the player *doesn't* have a score yet, then we need to establish
    # their score.
    else:
        scores[player] = score

    describe_game(circle, current_marble, scores, playing_marble)

    # Now we increment the playing_marble counter.
    playing_marble += 1

    # For players, we need to be a bit more careful; if we are at the
    # last player, the next player will be the first player.
    if player == players:
        player = 1
    # Otherwise, it's just the next player.
    else:
        player += 1

describe_game(circle, current_marble, scores, playing_)marble)
