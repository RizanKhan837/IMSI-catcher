from jimner import jimner
def print_banner():
    END = '\033[0m'
    print('')
    padding = '  '

    a=jimner()

    a.get_banner_from_text('ANSI Shadow','IMSI Catcher')
    a.get_banner_from_text('Calvin S','By')

    B = [   ['\t\t\t\t', '┬', '─', '', '┐'], 
            ['\t\t\t\t', '├', '─', '', '┤'], 
            ['\t\t\t\t', '┴', '─', '', '┘']
        ]

    I = [   [' ', '┬'], 
            [' ', '│'], 
            [' ', '┴']
        ]
    L = [   [' ', '┬',' ', ' '], 
            [' ', '│',' ', ' '], 
            [' ', '┴','─', '┘']
        ]	
    A = [   ['┌','─','┐'], 
            ['├','─','┤'], 
            ['┴',' ','┴']
        ]
    L2 = [  [' ', '┬',' ', ' '], 
            [' ', '│',' ', ' '], 
            [' ', '┴','─', '┘']
        ]	

    banner = [B,I,L,A,L2]
    final = []	
    init_color = 97
    txt_color = init_color
    cl = 0
		
    for charset in range(0, 3):
        for pos in range(0, len(banner)):
            for i in range(0, len(banner[pos][charset])):
                clr = f'\033[38;5;{txt_color}m'
                char = f'{clr}{banner[pos][charset][i]}'
                final.append(char)
                cl += 1
                txt_color = txt_color + 36 if cl <= 3 else txt_color

            cl = 0

            txt_color = init_color
        init_color += 1

        if charset < 2: final.append('\n   ')

    print(f"   {''.join(final)}")
    print(f'{END}{padding}           \n')
print_banner()