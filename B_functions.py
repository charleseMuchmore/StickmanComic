from os import system, name

def next_slide(slide, slide_text):
    """takes a slide and the corresponding text, prints slide first, and then the text below it"""
    print(slide)
    print(slide_text)

def clear():
    """Clears the terminal"""
    if name == 'nt':
        _=system('cls')
    else:
        _=system('clear')