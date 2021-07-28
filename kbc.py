question_list=["How many continents are there?", "What is capital of India?"]
option_list=[["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"]]
answer_list=[3,4]
fifty_list=[['1.Four','3.seven'],['2.Bhopal','4.Delhi']]
solution_list=[3,4]
print("Co-Powered by Dabur Amla presents,Kaun Banega Crorepati mein apka swagat hai!!")
print("Sadab,Aadab aur Shastriyakal.")
print("Pehla Question yeh rha apke screen ke upar:")
lifelinecount = 0
def lifeline(index):  
    global lifelinecount
    j=0 
    if(lifelinecount==0): 
        while j<len(fifty_list[index]):
            print("    ",fifty_list[index][j])
            j=j+1
        user_ans = int(input('choose your answer'))
        lifelinecount+=1
        if user_ans==solution_list[index]:
            return True
        else:
            return False
    else:
        print('you Already used 5050')
        return "no"
        
def option(index):
    j=0
    while j<len(option_list[index]):
        print("    ",option_list[index][j])
        j=j+1
    user_ans = int(input('choose  your answer='))
    if user_ans==answer_list[index]:
        return True
    if user_ans == 5050:
        return(lifeline(index))
    else:
        return False

def que():
    index=0
    while index<len(question_list):
        print("Q.",index+1,question_list[index])
        result=option(index)
        if result=="no":
            index=index+1
        elif result==True:
            print("congratulations")
        else:
            print("you loose")
            break   
        index=index+1

def main():
    que()
main()