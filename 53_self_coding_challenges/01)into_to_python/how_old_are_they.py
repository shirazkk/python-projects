"""
Problem Statement

Write a program to solve this age-related riddle!

Anton, Beth, Chen, Drew, and Ethan are all friends. Their ages are as follows:

Anton is 21 years old.

Beth is 6 years older than Anton.

Chen is 20 years older than Beth.

Drew is as old as Chen's age plus Anton's age.

Ethan is the same age as Chen.

"""

def main():
    Shiraz:int=21
    Ali:int=Shiraz+6
    Sarmad:int=Ali+20
    Salman:int=Sarmad+Shiraz
    Owais:int=Salman

    print(f'Shiraz is {str(Shiraz)} years old.')
    print(f'Ali is {str(Ali)} years old.')
    print(f'Sarmad is {str(Sarmad)} years old.')
    print(f'Salman is {str(Salman)} years old.')
    print(f'Owais is {str(Owais)} years old.')

if __name__ == '__main__':
    main()