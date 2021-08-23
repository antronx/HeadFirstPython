from time import sleep

word = "bottles"
for num in range(99 ,0 , -1):
    print(num, word, "of beer on the wall")
    print(num, word, "of bear")
    new_num = num -1
    if new_num == 0:
        print ("Take one down and pass it around, no more bottles of beer on the wall.")
    elif new_num==1:
        word = "bottle"
        print("Take one down and pass it around,", new_num, word, "of beer on the wall.")
    else:
        print("Take one down and pass it around,", new_num, word, "of beer on the wall.")
    sleep(0.5)
