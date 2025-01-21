import random
import pytest

def compute_average(values):
    return sum(values)/len(values)
         
def test_compute_average():
    values= [0,1,2,3]
    assert compute_average(values)==1.5

    random.seed(0)
    values = [random.randint(0,100) for _ in range(10)]
    assert compute_average(values)==55.3
def main():
        print(compute_average([1,2,3,7,8,33,12,-2])) #Should be 8.0

if __name__=="__main__":
     main()
     #this is a change