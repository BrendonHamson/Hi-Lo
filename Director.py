from Game.Cards import Cards

class Director:
    #The director is the card dealer or 'House'. Controlling the operations of the game.

    def ___init___(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.card1 = 0
        self.card2 = 0
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing == True:
            self.get_inputs()
            self.compare_cards()
            self.do_outputs()

    def get_inputs(self):
        """Show Player Card
        Player bets higher or Lower
        Show Dealer Card
        """
        print(f"Your card is {self.card1}")
        self.deal_card = input("Do you bet that the dealers card will be higher or lower? (H/L) ")
        print(f"The dealers card is {self.card2}")

        
       
    def compare_cards(self):
        """Compare cards to players bet
        Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        if self.deal_card.capitalize == "H":
            if self.card2 > self.card1:
                self.total_score -= 75
            else:
                self.total_score += 100
        else:
            if self.card1 > self.card2:
                self.total_score -= 75
            else:
                self.total_score += 100
     

    def do_outputs(self):
        """Show score
        Ask if player wants to play again
        Determine if player is able to play again
        """
        if not self.is_playing:
            return
        print(f"Your score is now: {self.total_score}")
        self.is_playing == (self.score > 0)

        play_again = input("Do you want to play again? (Y/N) ")
        if play_again.capitalize == "N":
            return

