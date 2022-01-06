label_series = Label(root, text="Fibonacci Series: " )
label_flower = Label(root)
label_sprial = Label(root)

def Fibonacci():
    num = 10

    first_no = 0
    second_no = 1
    sum = 0
    counter = 1
    while (counter <= num):
        label_series["text"] += str(sum) + " "
        counter = counter + 1
        first_no = second_no
        second_no = sum
        sum = first_no +second_no