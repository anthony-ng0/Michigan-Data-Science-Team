"""
MDST Workshop 1 - Python Basics Starter Code
"""

# Add any imports you need here:
from random import randrange
from base64 import b64encode
from base64 import b64decode
def part1(num):
    """
    Ask the user for a number. Depending on whether the number is even or odd,
    print out an appropriate (i.e. "even" or "odd") message to the user.
    """
    if (num % 2 == 0):
        print("even!")
    else:
        print("odd!")


def part2():
    """
    Generate a random number between 1 and 9 (including 1 and 9). Ask the user
    to guess the number, then tell them whether they guessed too low, too high,
    or exactly right.
    (Hint: remember to use the user input lessons from the very first
    exercise).
    Keep the game going until the user types "exit".
    [ try checking the random module in python on google. Concepts: Infinite
    loops, if, else, loops and user/input].
    """
    rand_num = randrange(1,9)
    
    guess = input("Guess: ")
    while(guess != "exit"):
        if (int(guess) < rand_num):
            print("Too low")
        elif(int(guess) > rand_num):
            print("Too high")
        elif (guess == "exit"):
            break
        else:
            print("You got it!")
            rand_num = randrange(1,9)
        guess = input("Guess: ")
        

def part3(string):
    """
    Ask the user for a string and print out whether this string is a palindrome
    or not. (A palindrome is a string that reads the same forwards and
    backwards.)
    """
    if (string == string[::-1]):
        print("True")
    else:
        print("False")


def part4a(filename, username, password):
    """
    Encrypt your username and password using base64 module
    Store your encrypted username on the first line and your encrypted password
    on the second line.
    """
        
    user_bytes = username.encode("ascii")
    pass_bytes = password.encode("ascii")
    encrypted_user = b64encode(user_bytes)
    encrypted_pass = b64encode(pass_bytes)
    encrypted_user_ascii = encrypted_user.decode('ascii')
    encrypted_pass_ascii = encrypted_pass.decode('ascii')
    fp = open(filename, 'w')
    fp.write(str(encrypted_user_ascii) + "\n")
    fp.write(str(encrypted_pass_ascii))
    fp.close()
    

def part4b(filename, password=None):
    """
    Create a function to read the file with your login information.
    Print out the decrypted username and password.
    If a password is specified, update the file with the new password.
    """
    
    fp = open(filename, 'r')
    encrypted_user_ascii = fp.readline()
    encrypted_pass_ascii = fp.readline()
    
    encrypted_user = encrypted_user_ascii.encode("ascii")
    encrypted_pass = encrypted_pass_ascii.encode('ascii')
    
    decrypted_user = b64decode(encrypted_user)
    decrypted_pass = b64decode(encrypted_pass)
    
    user = decrypted_user.decode('ascii')
    password1 = decrypted_pass.decode('ascii')
    
    print("Username: " + user)
    print("Password: " + password1)
    fp.close()
    
    if (password != None):
        pass_bytes = password.encode("ascii")
        encrypted_pass = b64encode(pass_bytes)
        encrypted_pass_ascii = str(encrypted_pass.decode('ascii'))
        
        fp = open(filename, 'r')
        temp_user = fp.readline()
        temp_pass = encrypted_pass_ascii
        info_str = temp_user + temp_pass
        fp.close()
        fp = open(filename, 'w')
        fp.write(info_str)
        fp.close()
     
    
    
if __name__ == "__main__":
    part1(3)  # odd!
    part1(4)  # even!
    part2()
    part3("ratrace")  # False
    part3("racecar")  # True
    part4a("secret.txt", "naitian", "p4ssw0rd")
    part4b("secret.txt")
    part4b("secret.txt", password="p4ssw0rd!")
    part4b("secret.txt")
