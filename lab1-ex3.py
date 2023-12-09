# Write a program that will take as input a positive natural number and return the next smaller number from the same digits

input_num = input("Give natural number: ")

number = [char for char in input_num]

index_of_smallest_digit = 0
next_smaller_digit = len(number)-1

        # 4123152456

if len(input_num) == 2:
    if int(number[0]) > int(number[1]):
        number[0], number[1] = number[1], number[0]
        
    print(''.join(number))
else:
    
    left_index = len(number)-2
    for right_index in range(len(number)-1, 0, -1):
        if right_index == 1 and number[right_index] != 0:
            if int(number[left_index]) > int(number[right_index]):
                index_of_smallest_digit = left_index;
                # number[right_index], number[left_index] = number[left_index], number[right_index]
                break
        elif right_index != 1:
            if int(number[left_index]) > int(number[right_index]):
                index_of_smallest_digit = left_index;
                # number[right_index], number[left_index] = number[left_index], number[right_index]
                break
        left_index = left_index-1
        
    while int(number[next_smaller_digit]) >= int(number[index_of_smallest_digit]):
        next_smaller_digit -= 1
    
    number[index_of_smallest_digit], number[next_smaller_digit] = number[next_smaller_digit], number[index_of_smallest_digit]
    # print(''.join(number))
    
    # print()
    
    rest_of_num = []
    if index_of_smallest_digit != 0:
        for i in range(index_of_smallest_digit+1, len(number)):
            rest_of_num.append(int(number[i]))
        rest_of_num.sort(reverse=True)
        
        i = 0
        for index in range(index_of_smallest_digit+1, len(number)):
            number[index] = str(rest_of_num[i])
            i = i+1
        
        print(''.join(number))
    else:
        print(input_num)
    
    
    

