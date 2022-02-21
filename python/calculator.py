def  Calculate( a,b,operation):
     a = int(a);
     b= int(b);
     if(operation == "+"):
         return a+b;
     elif(operation =="-"):
         return a-b;
     elif(operation =="/"):
         if(b == 0):
             print("Cant divide by zero");
             return;
         return a/b;
     elif(operation=="*"):
         return a*b;
     else:
        print("Invalid operator");


a = input("Enter a value:");
b = input("enter a value:");

op = input("enter an operation:");

print(Calculate(a,b,op));




