from game import Game

def main():
    game = Game()
    game.start_round()

    while True:
        # Show public state while the round is ongoing
        if game.is_over:
            state = game.get_full_state()
        else:
            state = game.get_public_state()

        print("\n--- STATE ---")
        print("Player:", state["player_cards"], "=", state["player_value"])
        print("Dealer:", state["dealer_cards"], "=", state["dealer_value"])
        print("Over?:", state["is_over"], "Result:", state["result"])

        if game.is_over:
            break


if __name__ == "__main__":
    main()
