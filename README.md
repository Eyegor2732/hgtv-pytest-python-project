# hgtv-pytest-python-project
It's just practical application to perform entries for HGTV Urban Oasis® sweepstakes on sister sites HGTV and FoodNetwork. Simple logic: just type email you registered with before, tap on entry buttons, scroll up/down, switch between frames.

I've created several asserts there: check if correct button s are shown, verify you did not enter already today.

Here I used POM to separate page objects and actions from the test file; inheritance from the BaseClass class to the test class, inheritance from HomePage class to HomePageActions class; fixtures in contest.py file for setup/tear down and for keeping data; logging.

It's a very useful time saving program.
