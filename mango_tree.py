row = int(input())
column =int(input())
tree_num = int(input())
if 0<tree_num<=row:
    print("True")
elif tree_num % row== 0:
    print("true")
elif tree_num % column+1 ==0:
    print("true")
else:
    print("false")

