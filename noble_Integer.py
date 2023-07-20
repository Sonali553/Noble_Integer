lst = list(map(int, input().split()))
def nobel_Integer(lst ):
 lst.sort(reverse = True)
 if lst[0] == 0:
   return 1
 for i in range(0, len(lst)):
    if(lst[i] != lst[i - 1]):
          c = i
    if c == lst[i]:
      return 1
 return -1
print(nobel_Integer([3, 2, 1, 3]))
print(nobel_Integer([1, 1, 3, 3]))
print(nobel_Integer(lst))
