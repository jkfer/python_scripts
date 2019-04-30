#!/usr/bin/python

# get a string fron the user and reverse it.


string = ''

while len(string) == 0:
    string = raw_input('Enter your string:')
    print('You entered: "%s"' % string)


def reverse():
    count = len(string) - 1
    output = ''
    while count >= 0:
        output += string[count]
        count = count - 1

    print('Reversed output is: "%s"' % output)



if __name__ == '__main__':
    reverse()
