def welcome():
    print("hi,how can i help you")
def goodbye():
    print("thank you for your wonderfull time , If you have any questions feel free to ask")
def question():
    response = {
        "what is your name?":"my name is bobby",
        "tell me a joke?":"what do you call something which has no body and no nose ... we call it nobody knows",
        "how old are you?":"I do not have any age ",
        "who  created you?":"I was created by a goodb team of developer",
        "when will be ram mandir will be opened?":"jan 24,2024"
        
    }
    return response.get("I am not sure how to answer this question sorry!!!")
def chatbot():
    welcome()
    for i in range(5):
        user=input("you:")
        if "bye"in user:
            goodbye()
            break
        response=response_to_user(user)
        print("bot :",response)
chatbot()
            