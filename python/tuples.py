

## Tuple items are ordered, unchangeable, and allow duplicate values
## tuples
print(" -----------------------");
print(" working on tuples");
print(" -----------------------");
tup = (1,2,3);
tup[0];
tup[-1];
tup[1:3];

## unpacking tuples
(apple,banana,orange)= tup

fruits = tup;
print(apple)

tup1 =(1,2,3,4,5,6)
## ifn not equal
(apple,banana,orange,*peach)= tup1

print (peach) ## this is stored as a list

print("looping tuples")

for x in tup1:
    print(x)

## joun tuples
tup3 = tup1 +tup
print(tup3);

## multiply tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple);