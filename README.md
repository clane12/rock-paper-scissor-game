🎮 Rock Paper Scissors (Python CLI Game)
A simple command-line Rock, Paper, Scissors game written in Python. This game lets a user play against the computer in a quick, interactive session that repeats until the user quits.

✨ Features
💻 Command-line based

🧠 Randomized computer move

🥇 Win/loss/tie outcome detection

🔁 Supports multiple rounds in a loop

✅ Input validation included

🧰 How It Works
The game prompts the player to start by pressing 1 or exit with 2.

Once started, the user selects:

0 for rock

1 for paper

2 for scissor

The computer randomly selects one of the three.

The game compares choices and announces:

Win

Loss

Tie

Or invalid input

The user is then asked if they want to play another round.

📦 Requirements
Python 3 (any version 3.6+ works)

No external libraries required

🚀 How to Run
Save the script as rock_paper_scissors.py

Run it using the terminal:
python rock_paper_scissors.py
Follow on-screen prompts to play!

💡 Sample Output
press 1 to play the game, press 2 to quit: 1
select 1,2,3 based on rock, paper or scizzor:
1
you choose
paper

computer choose
rock
you win

want to play another round press 1 to start and 2 to stop: 2
game stopped
🔮 Potential Improvements
Add score tracking for both player and computer

Use string input ("rock", "paper", "scissor") instead of numbers

Add emoji-based feedback (🪨📄✂️)

Add a GUI with tkinter or PyQt
