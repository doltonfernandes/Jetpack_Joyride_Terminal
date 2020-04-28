##1. Rules of the game

	1) Game runs for a fixed amount of time which when exceeded makes you lose the game
	2) Many coins come on the way which when collected fetches you 5pts
	3) Kill enemies or obstacles to gain 2pts
	4) You get 3 lives
	5) Many Power(ups/downs) like shield , Magnets , Boost come on the way which can be collected
	6) In the end is the boss level. The boss shoots snow balls which need to be dodged
	7) Ultimate Dragon powerup can be used between the game
	8) Boss follows the mandalorian along the vertical axis
	9) To kill Boss, it needs to be hit by 10 bullets

##2. Description of Main Classes

	1) Board : Contains the main 2d numpy grid, timer, description, rules of the game.
	2) Game : This is where the main loop of the game runs and all other classes are called.

##3. Instructions to play

	Run the following command in the directory :	
	1) python3 main.py

	2) Use the following controls:
		a) w,a,d to move up, move left, move right respectively.
		b) 'space' to use shield
		c) l to shoot bullets
		d) Press Q to quit the game
		e) Press 0 to activate Ultimate Dragon which can be used only once in the entire game

##4. Requirements

	1) Python3
	2) colorama==0.4.3
	3) numpy==1.18.1

##How the OOPS concepts are used :

##1) Inheritance:

	As you can see in images ( images/1.png and images/2.png ) the class Enemy is inherited from two classes Person and Parent_Func.
	Some variables are kept protected beacause private variables can’t be accessed in an inherited class.

##2) Polymorphism :

	( images/3.png )
	This the class for the bars (obstacles)
	According to the value of p given during initialisation of the object of this class ,one of the 4 types of bars ( Vertical , Horizontal , Upper left to Lower right Diagonal , Upper right to Lower left Diagonal ) is made.

### 3) Encapsulation :

	Classes and object are being used and made so encapsulation is done.

### 4) Abstraction :

	( images/4.png )
	This is the Mandalorian class.
	We can see that functions like move left, move right etc are made to stow away inner details from the end user.
