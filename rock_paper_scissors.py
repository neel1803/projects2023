import random
from collections import Counter
def play(player1, player2, num_games, verbose=False):
    p1_prev_play = ""
    p2_prev_play = ""
    results = {"p1": 0, "p2": 0, "tie": 0}

    for _ in range(num_games):
        p1_play = player1(p2_prev_play)
        p2_play = player2(p1_prev_play)

        if p1_play == p2_play:
            results["tie"] += 1
            winner = "Tie."
        elif (
            (p1_play == "P" and p2_play == "R")
            or (p1_play == "R" and p2_play == "S")
            or (p1_play == "S" and p2_play == "P")
        ):
            results["p1"] += 1
            winner = "Player 1 wins."
        elif (
            p2_play == "P"
            and p1_play == "R"
            or p2_play == "R"
            and p1_play == "S"
            or p2_play == "S"
            and p1_play == "P"
        ):
            results["p2"] += 1
            winner = "Player 2 wins."

        if verbose:
            print("Player 1:", p1_play, "| Player 2:", p2_play)
            print(winner)
            print()

        p1_prev_play = p1_play
        p2_prev_play = p2_play

    games_won = results["p2"] + results["p1"]

    if games_won == 0:
        win_rate = 0
    else:
        win_rate = results["p1"] / games_won * 100

    print("Final results:", results)
    print(f"Player 1 win rate: {win_rate}%")

    return win_rate
def quincy(prev_play, counter=[0]):
    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]
def mrugesh(prev_opponent_play, opponent_history=[]):
    opponent_history.append(prev_opponent_play)
    last_ten = opponent_history[-10:]
    most_frequent = max(set(last_ten), key=last_ten.count)

    if most_frequent == "":
        most_frequent = "S"

    ideal_response = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[most_frequent]
def kris(prev_opponent_play):
    if prev_opponent_play == "":
        prev_opponent_play = "R"
    ideal_response = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[prev_opponent_play]
def abbey(
    prev_opponent_play,
    opponent_history=[],
    play_order=[
        {
            "RR": 0,
            "RP": 0,
            "RS": 0,
            "PR": 0,
            "PP": 0,
            "PS": 0,
            "SR": 0,
            "SP": 0,
            "SS": 0,
        }
    ],
):
    if not prev_opponent_play:
        prev_opponent_play = "R"
    opponent_history.append(prev_opponent_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1

    potential_plays = [
        prev_opponent_play + "R",
        prev_opponent_play + "P",
        prev_opponent_play + "S",
    ]

    sub_order = {
        k: play_order[0][k] for k in potential_plays if k in play_order[0]
    }
    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {"P": "S", "R": "P", "S": "R"}
    return ideal_response[prediction]
def human(prev_opponent_play):
    play = ""
    while play not in ["R", "P", "S"]:
        play = input("[R]ock, [P]aper, [S]cissors? ")
        print(play)
    return play
def random_player(prev_opponent_play):
    return random.choice(["R", "P", "S"])

counter_move = {"R": "P", "P": "S", "S": "R"}

steps = {}

def player(prev_play, opponent_history=[]):
  if prev_play != "":
      opponent_history.append(prev_play)

  # Interestingly, 3 to 6 works best, as in we win more than 60%.
  # If n is larger than 6, we start to get terrible result.
  # I guess it's becauase we don't have enough data to predict once n get that
  # larger, we only play 1000 games.
  n = 5

  hist = opponent_history

  guess = "R"
  if len(hist) > n:
      pattern = join(hist[-n:])

      if join(hist[-(n + 1):]) in steps.keys():
          steps[join(hist[-(n + 1):])] += 1
      else:
          steps[join(hist[-(n + 1):])] = 1

      possible = [pattern + "R", pattern + "P", pattern + "S"]

      for i in possible:
          if not i in steps.keys():
              steps[i] = 0

      predict = max(possible, key=lambda key: steps[key])

      if predict[-1] == "P":
          guess = "S"
      if predict[-1] == "R":
          guess = "P"
      if predict[-1] == "S":
          guess = "R"

  return guess


def join(moves):
  return "".join(moves)


play(player, quincy, 1000)
play(player, mrugesh, 1000)
play(player, abbey, 1000)
play(player, kris, 1000)
  
