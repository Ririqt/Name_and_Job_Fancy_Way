from pyfiglet import Figlet

font = Figlet(font="epic")
your_name = str(input("Enter Your Name: "))
your_dream_job = str(input("Enter Your Dream Job: "))

text_art = (font.renderText(your_name + " " + your_dream_job))
print('\033[95m' + text_art)
