from game import *
import signal

def signal_handler(sig, frame):
	pass

signal.signal(signal.SIGINT, signal_handler)

system("stty -echo")
system("clear")

if __name__ == "__main__":
	Wel.print_welcome_screen()
	inp = input()
	system("clear")
	game.start_game()