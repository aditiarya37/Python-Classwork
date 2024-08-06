names = ["Rapunzel", "Ariel", "Else", "Anna", "Aurora", "Cindrella"]
n = int(input("Enter the length: "))
len_names = [len(i) for i in names]
for j in range(len(names)):
    if len_names[j]>=n:
        print(names[j])
