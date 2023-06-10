#РЕШЕНИЕ ЗАДАЧ НА O(N**2)#

#def strcounter(s):
    #for i in s:
        #counter=0
        #for ii in s:
            #if i==ii:
                #counter+=1
        #print(i,counter)

#O(N*M)#
#def strcounter(s):
    #for x in set(s):
        #counter=0
        #for xs in s:
            #if x==xs:
                #counter+=1
        #print(x,counter)
#strcounter('abcddddd')

#O(N) или O(2N)=O(N)
#def strcounter(s):
    #lits_counter={}
    #for lit in s:
        #lits_counter[lit]=lits_counter.get(lit,0)+1
    #for lits, counter in lits_counter.items():
        #print(lits,counter)

#def strcounter(s):
    #return {x:s.count(x) for x in set(s)}
#print(strcounter('sadjasljdaslkjalkjaew'))