import tkinter as tk
from tkinter import ttk
import random

class BlackjackApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack")
        self.master.geometry("400x300")

        self.deck = self.create_deck()
        self.player_hand = []
        self.dealer_hand = []

        self.create_widgets()

    def create_deck(self):
        deck = [('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10), ('Valet', 10),
                ('Dame', 10), ('Roi', 10), ('As', 11)] * 4
        random.shuffle(deck)
        return deck

    def deal_card(self):
        return self.deck.pop()

    def deal_initial_cards(self):
        self.player_hand = [self.deal_card(), self.deal_card()]
        self.dealer_hand = [self.deal_card(), self.deal_card()]

    def calculate_hand_value(self, hand):
        value = sum(card[1] for card in hand)
        num_aces = sum(1 for card in hand if card[0] == 'As')
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value

    def hit(self):
        self.player_hand.append(self.deal_card())
        player_score = self.calculate_hand_value(self.player_hand)
        self.player_score_label.config(text=f"Score du Joueur : {player_score}")
        if player_score > 21:
            self.outcome_label.config(text="Le joueur dépasse 21! La banque gagne.")

    def stand(self):
        player_score = self.calculate_hand_value(self.player_hand)
        dealer_score = self.calculate_hand_value(self.dealer_hand)
        while dealer_score < 17:
            self.dealer_hand.append(self.deal_card())
            dealer_score = self.calculate_hand_value(self.dealer_hand)

        self.dealer_score_label.config(text=f"Score de la Banque : {dealer_score}")
        if dealer_score > 21 or player_score > dealer_score:
            self.outcome_label.config(text="Le joueur gagne!")
        elif dealer_score > player_score:
            self.outcome_label.config(text="La banque gagne!")
        else:
            self.outcome_label.config(text="Égalité!")

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', font=('Arial', 12), padding=5)
        style.configure('TLabel', font=('Arial', 12), padding=5)

        self.player_score_label = ttk.Label(self.master, text="")
        self.player_score_label.pack()

        self.dealer_score_label = ttk.Label(self.master, text="")
        self.dealer_score_label.pack()

        self.hit_button = ttk.Button(self.master, text="Piocher", command=self.hit)
        self.hit_button.pack()

        self.stand_button = ttk.Button(self.master, text="Rester", command=self.stand)
        self.stand_button.pack()

        self.outcome_label = ttk.Label(self.master, text="")
        self.outcome_label.pack()

        self.deal_initial_cards()

        player_score = self.calculate_hand_value(self.player_hand)
        dealer_score = self.dealer_hand[0][1]  # Montrer seulement la première carte du croupier
        self.player_score_label.config(text=f"Score du Joueur : {player_score}")
        self.dealer_score_label.config(text=f"Score de la Banque : {dealer_score}")

root = tk.Tk()
app = BlackjackApp(root)
root.mainloop()

