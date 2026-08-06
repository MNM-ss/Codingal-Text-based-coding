total_homework = 4 
original_count = total_homework 
print(f"You have {original_count} homeworks and tasks to finish today!\n") 


completed_count = 0 
HW_num = 1 


while HW_num <= total_homework: 
    if HW_num == 1: 
        next_HW = "Your Argumentative Essay" 
    elif HW_num == 2: 
        next_HW = "Math Practise" 
    elif HW_num == 3: 
        next_HW = "History and Geography projects" 
    else: 
        next_HW = "Coding H.W" 
        
    
    answer = input(f"Have you finished: {next_HW}? (yes/no): ") 
    
    
    if answer == "yes": 
        completed_count += 1 
        HW_num += 1 
        print("Great job! Task completed.") 
    else: 
        print("Okay, finish it and check again!") 
        
    
    print("Homeworks and tasks remaining:", total_homework - completed_count) 
    print() 


print("===== ALL TASKS COMPLETE!!! =====") 
print("Great work finishing your entire checklist today!\n") 


print("Now let's look as an infinite loop") 
test_value = 0 
safety_counter = 0 
while test_value <= 0: 
    print("This condition never changes, so this would run forever") 
    safety_counter += 1 
    if safety_counter == 3: 
        print("(Stopping here on purpose or else it will hang!)") 
        break 


print("\n===== H.W and TASKS CHECKLIST SUMMARY =====") 
print("HW and TASKS Assigned Today:", original_count) 
print("HW and TASKS Completed:", completed_count) 
print("HW and TASKS Remaining:", total_homework - completed_count)
print("=======================")
