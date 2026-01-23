# Python 3.14.2
import os

def main():
    win_prob = float(input("Enter win probability as decimal: "))
    lose_prob = float(input("Enter lose probability as decimal: "))
    gains = float(input("Enter gains per win: "))
    losses = float(input("Enter losses per loss: "))
    expected_value = (win_prob * gains) - (lose_prob * losses)
    print(f"Expected Value: {expected_value}\n\n")

if __name__ == "__main__":
    os.system('cls')
    while True:
        main()