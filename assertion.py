# assert condition, message
# if oncidtion true ---> move on 
# if condition fales --> AssertionError with message 

def avg(nums):
    assert len(nums)>0, "nums must not be empty "
    return sum(nums)/len(nums)

print(avg([]))

# exceptions ---> runtime error
# assertion ---> programmer's mistake during development 

# user facing errors ---> use exceptions or check explicitly
# use assertion ---> documentation, check assumptions with input invariants


