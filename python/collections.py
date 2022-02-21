## python collections are list,tuple,set,dcitionary


## list
friends =["kevin","karen","adasd",1]

print(friends);
print(friends[0]);
print(friends[-1]);
print(friends[-2]);

print(friends[1:3]);


## dictinoaries
monthconversions ={

"jan": "january",
"feb" : "February"

}



print(monthconversions);

print(monthconversions["jan"]);

print(monthconversions.get("jan"));

print(monthconversions.get("sfsd","not a valid key"));

try:
    print(monthconversions("adas"));
except:
    print("Key not found");



### sets
set1 ={1,2,3};
print (set1);

set1 ={1,2,3,3};## duplicates will be ignored, you cant change existing item,but can remove or add 