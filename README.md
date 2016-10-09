# FroggerClone
This is a clone of Frogger done in Python 2.7 using PyGame.

# Setup

* Python 2.7.9

* [PyGame] (https://bitbucket.org/pygame/pygame/downloads)

# Screenshot

<img src="https://raw.githubusercontent.com/sedentaryseal/FroggerClone/master/screenshots/frogger_screenshot.PNG" />

# Bugs

* If you get off a log and then get back on it, the log won't be detected and you'll lose a life

* Collision with vehicles only works occasionally, normally when you try to move and collide with one. Does not work if the vehicle hits you when you are stationary.

* When trying to get off one of the logs, you will continue to move at the same speed as the log, just on the column you moved to.