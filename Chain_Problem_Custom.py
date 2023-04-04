def printTable(coins):
    for i in range(len(coins)):
     print()
     for j in range(len(coins[i])):
         print(coins[i][j],end="  ")
         
def start(Coins):
    deno=[]
    n= int(input("How much money are you splitting?> "))
    main(n,Coins,1000)

    
def main(n, Coins, r):
    global table
    table=[[]]
    for i in range(r):
        table.append([])
        table[i]=[0]*(n+1)
    for i in range(n):
        table[0][i+1]=(n+1)
        
    for j in range(len(table[0])-1):
        i=0
        for i in range(len(Coins)):
            q= j+1
            if  q-Coins[i] >= 0:
                if (table[0][q-Coins[i]]+1) < table[0][q]:
                    if table[0][q-Coins[i]] != 0:
                        for k in range(table[0][q-Coins[i]]):
                            y= k+1
                            if table[y][q-Coins[i]] !=0:
                                table[y][q]=table[y][q-Coins[i]]
                                table[y+1][q]=Coins[i]
                            else:
                                break
                    else:
                        table[1][q]=Coins[i]
                            
                table[0][q] = min(table[0][q-Coins[i]]+1, table[0][q])

    for i in range(len(table[0])-1):
        q=i+1
        for j in range(len(table)-1):
            if table[0][q] < j:
                table[j][q] = 0
    deno=[]
    for i in range(len(table)-1):
        try:
            if table[i+1][n] != 0:
                deno.append(table[i+1][n])
        except:
            break
    group(deno, Coins)

        
def group(deno, Coins):
    final=[[]]
    for i in range(len(Coins)-1):
        final.append([])
        
    for i in range(len(Coins)):
        for j in range(len(deno)):
            if deno[j] == Coins[i]:
                final[i].append(deno[j])
    finish(final)


def finish(final):
    print("The denominations you will need are...")
    for i in range(len(final)):
        try:
            print(str(len(final[i])) + str(" ") + str(final[i][0]))
        except:
            continue

            

Coins = (1, 5, 18, 25)
start(Coins)
