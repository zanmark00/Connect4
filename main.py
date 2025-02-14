import time  # Import the time module

from players import PlayerManager, DefaultPlayer, QLearningPlayer, MinimaxPlayer
from minimax import MinimaxStrategy
from game import Game
from qlearning import QLearningStrategy
from board import Board

def run_iterations(player1, player2, num_iterations):
    results = {'X': {'wins': 0, 'losses': 0, 'draws': 0}, 'O': {'wins': 0, 'losses': 0, 'draws': 0}}
    for _ in range(num_iterations):
        game = Game(player1, player2)
        game.play()
        winner = game.get_winner()
        if winner is None:
            results[player1.get_token()]['draws'] += 1
            results[player2.get_token()]['draws'] += 1
        else:
            results[winner]['wins'] += 1
            loser = 'O' if winner == 'X' else 'X'
            results[loser]['losses'] += 1
    return results

def create_player(player_manager, player_type, token, **kwargs):
    if player_type == 'qlearning':
        q_learning_args = {k: v for k, v in kwargs.items() if k in ['learning_rate', 'discount_factor', 'epsilon']}
        strategy = QLearningStrategy(token=token, **q_learning_args)
        player = QLearningPlayer(token, strategy)
    elif player_type == 'minimax':
        use_alpha_beta = kwargs.get('use_alpha_beta', True)
        strategy = MinimaxStrategy(token, use_alpha_beta=use_alpha_beta)
        player = MinimaxPlayer(token, strategy)
    elif player_type == 'default':
        player = DefaultPlayer(token)
    return player

def train_qlearning_player(player, num_train_episodes, game):
    if isinstance(player, QLearningPlayer):
        start_time = time.time()  # Start timing
        player.strategy.train(game, num_train_episodes)
        end_time = time.time()  # End timing
        training_time = end_time - start_time
        print(f"Training completed in {training_time:.2f} seconds.")
        return training_time
    else:
        print("Player is not a QLearningPlayer. Cannot train.")
        return 0

def main():
    player_manager = PlayerManager()
    valid_strategies = ['minimax', 'qlearning', 'default']
    total_training_time = 0 

    # Player 1 setup
    print("Select player 1 strategy ('minimax', 'qlearning', 'default'):")
    player1_type = input().strip().lower()
    while player1_type not in valid_strategies:
        print(f"Invalid strategy. Please choose from: {', '.join(valid_strategies)}")
        player1_type = input().strip().lower()

    use_alpha_beta_p1 = False
    if player1_type == 'minimax':
        print("Use alpha-beta pruning for player 1? (yes/no):")
        use_alpha_beta_p1 = input().strip().lower() == 'yes'
    kwargs_p1 = {'use_alpha_beta': use_alpha_beta_p1} if player1_type == 'minimax' else {}
    player1 = create_player(player_manager, player1_type, 'X', **kwargs_p1)

    # Player 2 setup
    print("Select player 2 strategy ('minimax', 'qlearning', 'default'):")
    player2_type = input().strip().lower()
    while player2_type not in valid_strategies:
        print(f"Invalid strategy. Please choose from: {', '.join(valid_strategies)}")
        player2_type = input().strip().lower()

    use_alpha_beta_p2 = False
    if player2_type == 'minimax':
        print("Use alpha-beta pruning for player 2? (yes/no):")
        use_alpha_beta_p2 = input().strip().lower() == 'yes'
    kwargs_p2 = {'use_alpha_beta': use_alpha_beta_p2} if player2_type == 'minimax' else {}
    player2 = create_player(player_manager, player2_type, 'O', **kwargs_p2)

    game = Game(player1, player2)

    # Train Q-learning player(s)
    if player1_type == 'qlearning':
        print("Enter the number of training episodes for player 1:")
        num_train_episodes = int(input())
        training_time = train_qlearning_player(player1, num_train_episodes, game)
        total_training_time += training_time

    if player2_type == 'qlearning':
        print("Enter the number of training episodes for player 2:")
        num_train_episodes = int(input())
        training_time = train_qlearning_player(player2, num_train_episodes, game)
        total_training_time += training_time

    print(f"Total training time: {total_training_time:.2f} seconds.")

    print("Enter the number of game iterations to play:")
    num_iterations = int(input())

    results = run_iterations(player1, player2, num_iterations)
    print("\nResults:")
    for player_token, stats in results.items():
        print(f"Player {player_token}: Wins: {stats['wins']}, Losses: {stats['losses']}, Draws: {stats['draws']}")

if __name__ == "__main__":
    main()
