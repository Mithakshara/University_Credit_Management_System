# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution. 
# Student ID: w1899343
 
# Date: 2022.04.18


Total_count=0
count_progress=0
count_trailer=0
count_retriever =0
count_excluded = 0

Pass_list=[]
Defer_list=[]
Fail_list=[]
outcome_list=[]

print('Staff Version with Histogram \n')

while True:
    while True:
        
        while True:
            try:
                Pass=int(input('Please enter your credits at Pass: '))
                if Pass == 0 or Pass ==20 or Pass ==40 or Pass ==60 or Pass ==80 or Pass ==100 or Pass ==120:            
                    break
                else:
                    print('Out of range \n')           
            except ValueError:
                print('Integer required \n')

        while True:
            try:
                Defer=int(input('Please enter your credit at Defer: '))
                if Defer == 0 or Defer ==20 or Defer ==40 or Defer ==60 or Defer ==80 or Defer ==100 or Defer ==120:            
                    break
                else:
                    print('Out of range \n')

            except ValueError:
                print('Integer required \n')

        while True:
            try:
                Fail=int(input('Please enter your credit at Fail: '))
                if Fail == 0 or Fail ==20 or Fail ==40 or Fail ==60 or Fail ==80 or Fail ==100 or Fail ==120:
                    break
                else:
                    print('Out of range \n')
            except ValueError:
                print('Integer required \n')


     
        Total = Pass + Defer + Fail
        if Total == 120:
            break
        else:
            print('Total incorrect \n')
            continue
        

    if Pass == 120 and Defer == 0 and Fail == 0:
        print('Progress')
        count_progress = count_progress + 1
        outcome_list.append('Progress')

    elif Pass == 100 and Defer <=20 and Fail <= 20:
        print('Progress (module trailer) ')
        count_trailer =count_trailer + 1
        outcome_list.append('Progress (module trailer)')

    elif 80 >= Pass >= 40 and Defer <= 80  and Fail <= 60:
        print('Do not Progress – module retriever')
        count_retriever =count_retriever + 1
        outcome_list.append('module retriever')

    elif Pass ==40 and Defer == 0 and Fail == 80:
        print('Excluded')
        count_excluded = count_excluded + 1
        outcome_list.append('Excluded')

    elif Pass == 20 and 40 <= Defer <= 100 and Fail <= 60:
        print('Do not progress – module retriever')
        count_retriever =count_retriever + 1
        outcome_list.append('module retriever')

    elif Pass == 20 and Defer <= 20 and Fail <= 60 :
        print('Excluded ')
        count_excluded = count_excluded + 1
        outcome_list.append('Excluded')
        
    elif Pass == 0 and Defer >=60 and Fail >= 60:
        print('Do not progress – module retriever')
        count_retriever =count_retriever + 1
        outcome_list.append('module retriever')

    else :
        print('Excluded ')
        count_excluded = count_excluded + 1
        outcome_list.append('Excluded')


    Total_count=Total_count + 1
    print('\n')

    Pass_list.append(Pass)
    Defer_list.append(Defer)
    Fail_list.append(Fail)
    
    print('Would you like to enter another set of data?')
    option=input("Enter 'y' for yes or 'q' to quit and view results: ")

    if option == 'y' :
        continue
           
    elif option == 'q':
        break
    

print('------------------------------------------------------------------------------')
print('Horizontal Histogram')
print('Progress   ',count_progress,'  :','*' * count_progress)
print('Trailer    ',count_trailer ,'  :','*' * count_trailer)
print('Retriever  ',count_retriever,'  :','*' * count_retriever)
print('Excluded   ',count_excluded,'  :','*' * count_excluded)
print(Total_count,'outcomes in total')
print('------------------------------------------------------------------------------')

print('------------------------------------------------------------------------------')
print('Vertical Histogram')
header =[' Progress ',' Trailer ',' Retriever ',' Excluded ']
print(''.join(header))
for x in range(max(count_progress, count_trailer, count_retriever, count_excluded)):
    print(" {0} {1} {2} {3} ".format(
        '   *     'if x < count_progress else '         ',
        '   *    'if x < count_trailer else '        ',
        '     *    'if x < count_retriever else '          ',
        '   *     'if x < count_excluded else '         '
        ))

print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')

#text file

f= open('file.txt','w')

for i in range(len(Pass_list)):

    f.write(f'{outcome_list[i]} - ')
    f.write(f'{Pass_list[i]}')
    f.write(f', {Defer_list[i]}')
    f.write(f', {Fail_list[i]}\n')
    
f= open('file.txt','r')
for line in f:
    print(line,end='')
f.close()
print('------------------------------------------------------------------------------')
print('------------------------------------------------------------------------------')
