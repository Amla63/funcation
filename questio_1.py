def eligible_for_vote(user):
    if user>=18:
        print("you are eligible ")
    else:
        print("not eligible")
user=int(input("enter the num"))
eligible_for_vote(user)