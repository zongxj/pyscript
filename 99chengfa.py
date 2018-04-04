#coding:utf-8

#九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        #print(i,'x',j,'=',i*j,end="\t")
        print('%sx%s=%s' %(i,j,i*j),end='\t')
        #print('{}x{}={}\t'.format(i, j, i * j), end='')
    print()