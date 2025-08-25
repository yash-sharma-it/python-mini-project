HISTORY_FILE = "history.txt"

def show_history():
    file = open(HISTORY_FILE, 'r') #read
    lines = file.readlines()
    if len(lines) == 0:
        print("No History Found")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()


def clear_history():
    file = open(HISTORY_FILE, 'w') #write
    file.close()
    print("History Cleared")

def save_to_history(equation, result):
    file = open(HISTORY_FILE, 'a') #alter
    file.write(equation + "=" + str(result) + "\n")
    file.close()

def calculate(user_input):
    parts = user_input.split() #to split the user input in seperate string , like if "2+2" , it become "2","+","2"
    if len(parts) != 3:
        print("Invalid input. Use format: number operator number(e.g 8 + 8)")
        return
    
    num1 = float(parts[0])
    op =parts[1]
    num2 = float(parts[2])

    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        if num2 == 0:
            print("Cannot divide by Zero")
            return
        result = num1 / num2
    else:
        print("Invalide Operator, Use only + - * /")
        return
    
    if int(result) == result: # if ans is 4.0 then this line convert it into 4 .
        result =int(result)

    print("Result" , result)
    save_to_history(user_input, result)

def main():
    print(" ---- SIMPLE CALCULATOR (type history, clear or exit)")
    while True:
        user_input = input("Enter calculation (+ - * /) or command(history, clear, exit)")
        if user_input == "exit":
            print("GOOD BYE")
            break
        elif user_input == "history":
            show_history()
        elif user_input == "clear":
            clear_history()
        else:
            calculate(user_input)

main()
    