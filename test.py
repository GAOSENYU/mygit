def  hanoi(n,x,y,z):
    if  n==1:
        print (x,'-->',z)
    else:
        hanoi(n-1,x,z,y)#将前n1个盘子从x移动到哦y上
        print(x,'-->',z)#将最底下的最后一个盘子从x移动到z上
        hanoi(n-1,y,z,z)#将y上的n-1个盘子移动到z上

# n = int(input('请输入汉诺塔层数'))
hanoi(3,'x','y','z')
