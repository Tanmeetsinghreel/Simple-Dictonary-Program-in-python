# create a dictionary and take input from the user and return the meaning of the word from the dictionary
print("welcome to Tanmeets dictionary\n")
print("which word meaning will you want too---\n")
print("muted,immuted,accidial,agender,bitcoin")
print("type the word and press enter key____")

dictionary = {"muted":"can be change","immuted":"can not be change","accidial":"accidentally dials someone number"
      ,"agender":"person not identify mail or female","bitcoin":"a digital currency not require an intermediary"}

search = input()

print(dictionary[search])
print("thankyou for using the dictionary.")