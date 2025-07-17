to_do_list=[]
while True:
    task=input("enter a task (or 'done' to stop):")
    if task=='done':
      break
    else:
        to_do_list.append(task)
print("your task are:")
for task in to_do_list:
    print(task)