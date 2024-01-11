x = input('Please input an integer number: ')
y = input('Please input an integer number: ')
Odd_number_sum = 0
Even_number_sum = 0
while True:
    if x.isdigit() == True and y.isdigit() == True:
        count = int(x)
        end = int(y)
        while count <= end:
            if count%2 == 0 :
                Odd_number_sum += count
            else:
                Even_number_sum += count
            count += 1
    else:
        print("Unsupported operation")
        fresh_number = input('Would you like to quit (y/n)? ').upper()
        if fresh_number == "N":
            x = input('Please input an integer number: ')
            y = input('Please input an integer number: ')
        else:
            print("See you next time!")

    print(f'Odd number sum: {Odd_number_sum}')
    print(f'Even number sum: {Even_number_sum}')
