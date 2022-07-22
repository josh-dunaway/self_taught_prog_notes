def print_title():
   print('''
 ██░ ██  ▄▄▄       ███▄    █   ▄████  ███▄ ▄███▓ ▄▄▄       ███▄    █ 
▓██░ ██▒▒████▄     ██ ▀█   █  ██▒ ▀█▒▓██▒▀█▀ ██▒▒████▄     ██ ▀█   █ 
▒██▀▀██░▒██  ▀█▄  ▓██  ▀█ ██▒▒██░▄▄▄░▓██    ▓██░▒██  ▀█▄  ▓██  ▀█ ██▒
░▓█ ░██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒░▓█  ██▓▒██    ▒██ ░██▄▄▄▄██ ▓██▒  ▐▌██▒
░▓█▒░██▓ ▓█   ▓██▒▒██░   ▓██░░▒▓███▀▒▒██▒   ░██▒ ▓█   ▓██▒▒██░   ▓██░
 ▒ ░░▒░▒ ▒▒   ▓▒█░░ ▒░   ▒ ▒  ░▒   ▒ ░ ▒░   ░  ░ ▒▒   ▓▒█░░ ▒░   ▒ ▒ 
 ▒ ░▒░ ░  ▒   ▒▒ ░░ ░░   ░ ▒░  ░   ░ ░  ░      ░  ▒   ▒▒ ░░ ░░   ░ ▒░
 ░  ░░ ░  ░   ▒      ░   ░ ░ ░ ░   ░ ░      ░     ░   ▒      ░   ░ ░ 
 ░  ░  ░      ░  ░         ░       ░        ░         ░  ░         ░ 
                                                                     ''')

def print_hangman_stage(stage: int):
  if stage < len(list_of_hangman_figures):
    print(list_of_hangman_figures[stage])

list_of_hangman_figures = ['''
____ 
|/   | 
|   
|    
|    
|    
|
|_____''', '''
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____''', '''
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____''', '''
 ____
|/   |
|   (_)
|   \|
|    |
|    
|
|_____''', '''
 ____
|/   |
|   (_)
|   \|/
|    |
|    
|
|_____''', '''
 ____
|/   |
|   (_)
|   \|/
|    |
|   / 
|
|_____''', '''
 ____
|/   |
|   (_)
|   \|/
|    |
|   / \ 
|
|_____''', '''
 ____
|/   |
|   (_)
|   /|\ 
|    |
|   | |
|
|_____'''
]                                                                  

def print_winner():
  print('''
██╗    ██╗██╗███╗   ██╗███╗   ██╗███████╗██████╗     ██╗
██║    ██║██║████╗  ██║████╗  ██║██╔════╝██╔══██╗    ██║
██║ █╗ ██║██║██╔██╗ ██║██╔██╗ ██║█████╗  ██████╔╝    ██║
██║███╗██║██║██║╚██╗██║██║╚██╗██║██╔══╝  ██╔══██╗    ╚═╝
╚███╔███╔╝██║██║ ╚████║██║ ╚████║███████╗██║  ██║    ██╗
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝    ╚═╝
                                                        
''')

def print_loser():
  print('''
 ██▓     ▒█████    ██████ ▓█████  ██▀███  
▓██▒    ▒██▒  ██▒▒██    ▒ ▓█   ▀ ▓██ ▒ ██▒
▒██░    ▒██░  ██▒░ ▓██▄   ▒███   ▓██ ░▄█ ▒
▒██░    ▒██   ██░  ▒   ██▒▒▓█  ▄ ▒██▀▀█▄  
░██████▒░ ████▓▒░▒██████▒▒░▒████▒░██▓ ▒██▒
░ ▒░▓  ░░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░ ▒  ░  ░ ▒ ▒░ ░ ░▒  ░ ░ ░ ░  ░  ░▒ ░ ▒░
  ░ ░   ░ ░ ░ ▒  ░  ░  ░     ░     ░░   ░ 
    ░  ░    ░ ░        ░     ░  ░   ░     
                                          
''')

print(len(list_of_hangman_figures))