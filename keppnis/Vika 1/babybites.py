n = int(input())
words = input().split()

prints = "makes sense"
for i in range(n):
    if words[i] == str(i+1) or words[i] == "mumble":
        continue
    else:    
        prints = "something is fishy"
        break
print(prints)