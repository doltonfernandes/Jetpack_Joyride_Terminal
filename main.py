from game import *
import signal

def signal_handler(sig, frame):
	pass

signal.signal(signal.SIGINT, signal_handler)

if __name__ == "__main__":
	system("stty -echo")
	system("clear")
	system("mpg123 sounds/J.mp3 &")
	Wel.print_welcome_screen()
	inp = input()
	system("clear")
	game.start_game()