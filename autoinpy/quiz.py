quiz={
    "question1":{
        "question":"what is 3 +2 = ?",
        "answer":" 5"
    },
     "question2":{
        "question":"what is 4 - 9 = ?",
        "answer":" 5"
    },
     "question3":{
        "question":"what is 13 -3  = ?",
        "answer":" 10"
    },
     "question4":{
        "question":"what is 3 * 2= ?",
        "answer"  : " 6"
    },
     "question5":{
        "question":"what is 9 + 8= ?",
        "answer":" 17"
    },

}

score = 0
for key ,value in quiz.items():
    print (value['question']) 
    answer = input("answer? ")
    

    if answer == value['answer']:
        print('Correct')
        score = score +1
        print("Your sore is :" + str(score) )
    

    else :
        print("Wrong!")
        print("The answer is :" + value['answer'])
        print("Your score is :" + str(score))


print("You got" + score + "out of 5 question correctly")
print ("Your percontage is " + str(score /5 *100 ) + "%")