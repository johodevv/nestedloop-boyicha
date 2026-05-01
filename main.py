# ketma-ketlik
 
# n=10
# sum=0
 
# for x in range(1,10+1):
#     sum+=1/x
# print(sum)


# Geometrik shakl to'rt burchak

# n=5
# ssum=""
# s="*"
# for x in range (n):
#     ssum+=s
# for c in range(n):
#     print(ssum)


# sonlar juftligi

# n=5

# for x in range(0,n+1):
#     ssum=""
#     for j in range(0,n+1):
#         ssum+=(f"({x}.{j})")
#     print(ssum)


# Sonlar juftligi da C xarfi

# n=8

# for x in range (n+1):
#     ssum=""
#     for j in range (n+1):
#         if (x==0):
#             ssum+=(f"({x}.{j})")
#         if(x>0 and x<n):
#             ssum+=(f"({x}.{j})")
#             break
#         if(x==n):
#             ssum+=(f"({x}.{j})")
#     print(ssum)


# Sonlar juftligida ustunlar

# n=10 # berilgan son      

# for i in range(n):
#     for j in range(n):
#         if i==0 or i==9 or j%2== 0: 
#             print("({}, {}) ".format(i,j),end="")
#         else:
#             print("       ", end="");
#     print()    


# sonlar royhati

# n=5

# for x in range(0,n+1):

        
#     ssum=""
#     for j in range(0,n+1):
#         if x==0:
#             ssum+=(f"{j}  ")
#         else:
#             ssum+=(f"{x}{j} ")
#     print(ssum)



# diaganal

# n=5


# for x in range(n):
#     diaganal=""
#     for j in range(n):
#         if x==j:
#             diaganal+="*"
#         else:
#             diaganal+=" "
#     print(diaganal)

#sonlar diaganali 

# n=6
# for x in range(n+1):
#     diaganal=""
#     for j in range (n+1):
#         if x==j:
#             diaganal+=f"({x},{j})"
#         else:
#             diaganal+=" "
#     print(diaganal)


# teskari diaganal

# n=6


# for x in range(n,0,-1):
#     diaganal=""
#     for j in range (0,n):
#         if x==j:
#             diaganal+="*"
#         else:
#             diaganal+=" "
#     print(diaganal)


# Tog'ri burchakli uchburchak

# n=5
# ssum=""
# for i in range(n):
#     ssum+="*"
#     print(ssum)


# Teskari tog'ri burchakli uchburchak

# n=5
 
# for j in range(n,0,-1):
#     print("*"*j)

# Sonlar uchburchagi

# n=5
 
# n=5
# ssum=""

# for x in range(1,n+1):
#     for j in range(n+1):
#         if x==j:
#             ssum+=f"{j}"
#         else:
#             ssum+=""
#     print(ssum)


# Sonlar uchburchagi tartibli varianti

# n=5
# ssum=""

# for x in range(1,n+1):
#     for j in range(n+1):
#         if x==j:
#             ssum=f"{j}"*j
#         else:
#             ssum+=""
#     print(ssum)



# Parallelogram

# n=5

# for x in range(n):
#     ssum=""
#     for j in range(n):
#         if x==j:
#             ssum+="*"*5
#         else:
#             ssum+=" "
#     print(ssum)


# To'rtburchak qolibi

# n=5

# for x in range (n):
#     ssum=""
#     for j in range(1,n+1):
#         if x+j==n:
#             ssum+="b"
#     print(ssum) cholo 

# Diaganal va uchburchaklar


# n=5

# for x in range (n):
#     ssum=""
#     for j in range(n):
#         if x==j:
#             ssum+="*"
#         elif x<j:
#             ssum+="+"
#         elif x>j:
#             ssum+="-"
#     print(ssum)

# yulduzli x 
# keyinroq ishliman






# teskari parallelogram

# n=5

# for x in range (n):
#     ssum=""
#     for j in range(n):
#         if n-x==j:
#             ssum+="*"*n
#         else:
#             ssum+=" "
#     print(ssum)


# G'alati parallelogram
# keyinroq ishliman





# uchburchak


