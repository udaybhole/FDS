marks=[]
N=int(input("Enter total number of students:"))
print("Enter marks obtained by student in FDS:")
for i in range(N):
  m=int(input(""))
  marks.append(m)
print("marks of students are as follows:")
print(marks)
def avg():
 sum=0
 cnt=0
 for i in range(len(marks)):
    if marks[i]!=-1:
      sum=sum+marks[i]
      cnt+=1
 print("Total marks:",sum)
 print("Average of marks:",sum/cnt)

def absent():
 cnt=0
 for i in range(len(marks)):
     if marks[i]==-1:
       cnt+=1
 print("Count of student absent for test:",cnt)

def highest():
 high=marks[0]
 for i in range(len(marks)):
       if high<marks[i]:
            high=marks[i]
 print("highest score in class is:",high)

def lowest():
 low=marks[0]
 for i in range (len(marks)):
        if marks[i]==-1:
            continue
        if low>marks[i]:
                low=marks[i]
 print("Lowest score in class is:",low)

def maxFreq():
    i=0
    Max=0
    print("Marks  |  Frequency")
    for j in marks:
        if (marks.index(j)==i):
            print(j,"    |  ",marks.count(j))
            if marks.count(j)>Max:
                Max=marks.count(j)
                high_freq_mark=j
        i=i+1
    print("no of time max frquency",Max)
    print("the max frquency marks are",high_freq_mark)

if __name__ == "__main__":
 while True:
    print("Menu")
    print("1. Average Of Class: ")
    print("2. Highest score and lowest score of class: ")
    print("3. No. Of Absent Students: ")
    print("4. Highest Frequency Mark(s): ")
    print("5. Exit")
    choice = int(input("Enter Choice: "))
    if choice == 1:
      avg()
    elif choice == 2:
      highest()
      lowest()
    elif choice == 3:
      absent()
    elif choice == 4:
      maxFreq()
    elif choice == 5:
      exit()
    else:
      print("Invalid choice")
