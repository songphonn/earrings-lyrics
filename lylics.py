import sys
from rich import print
from time import sleep

def printLyrics():

    lines = [
        ("Her love is in your head", 0.06),
        ("You lost your earrings in her bed", 0.06),
        ("You couldn't tell her that you lost 'em", 0.05),
        ("'Cause you're scared and you're not talking", 0.05),
        ("So you think of what to say", 0.06),
        ("Then save it for another day", 0.06),
        ("'Cause you just never had the heart", 0.05),
        ("Now they just drift further apart", 0.05),
        ("From you.....", 0.08),

    ]
    
    
    delays = [0.8,0.6,0.5,0.7,0.8,0.5,0.6,0.4,3.0]

    for i, (line, char_delay) in enumerate(lines):
        for char in line:
            if line == '(Rock your body)':
                print(f"[orange4]{char}[/orange4]", end='')
            else:
               
                print(f"[bold][gold3]{char}[/gold3][/bold]", end='')
            
            sys.stdout.flush()
            sleep(char_delay)
            
        print()           
        sleep(delays[i])  


printLyrics()