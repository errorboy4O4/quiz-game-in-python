print("Hello and welcome to my Quiz Game!")
user_name = input("Please enter your name: ")
print("Hello ", user_name)
score = 0
play_or_not = input(f"{user_name}, do you want to start playing (yes or no): ").lower()
if play_or_not == "yes":
  print("Here's your first question:")
  ques1 = "Who is the Prime Minister Of India?"
  print(ques1)
  user1 = input("Your Answer: ").lower()
  ans1 = "narendra modi"
  if user1 == ans1:
    print("Congratulation, you get it correct!")
    score = score
  else:
    print("Opps, you get it incorrect: ")
    print("The correct answer is: ", ans1)
    print("Your score is: ", score)
  print("Here's your second question:")
  ques2 = "Who made Python language?"
  print(ques2)
  user2 = input("Your Answer: ").lower()
  ans2 = "guido van rossum"
  if user2 == ans2:
    print("Congratulation, you get it correct!")
    score+=1
  else:
    print("Opps, you get it incorrect: ")
    print("The correct answer is: ", ans2)
    score = score
else:
  print("Okay good bye, Have a nice day!")
print("Your total score is: ", score)
print("Good Bye!")



