def checkAge(age):
          if age >= 18:
                    return "You are allowed to vote!"
          else:
                    return "You are not allowed to vote."
Age = int(input("Enter your age: "))

sayIt = checkAge(Age)

print(sayIt)
