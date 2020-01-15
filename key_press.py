import sys,time
from select import select
from datetime import datetime

class Key_press:

	def key_press(self,argv,timeout):

	    # set raw input mode if relevant
	    # it is necessary to make stdin not wait for enter
	    try:
	        import tty, termios

	        prev_flags = termios.tcgetattr(sys.stdin.fileno())
	        tty.setraw(sys.stdin.fileno())
	    except ImportError:
	        prev_flags = None

	    buf = ''

	    c = ""

	    now = datetime.now()

	    while True: # main loop
	        rl, wl, xl = select([sys.stdin], [], [], timeout)
	        if rl: # some input
	            c = sys.stdin.read(1)
	            buf += c
	            # stop if 1 character is taken as input
	            if len(buf) >= 1:
	                break
	        else:
	            # timeout
	            break

	    # restore non-raw input
	    if prev_flags is not None:
	        termios.tcsetattr(sys.stdin.fileno(), termios.TCSADRAIN, prev_flags)

	    now = str(datetime.now() - now)
	    now = now.split(":")[2]
	    if timeout - float(now) > 0:
	    	time.sleep(timeout - float(now))
	    return c

K = Key_press()