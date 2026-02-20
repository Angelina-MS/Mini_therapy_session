name=input("what is your name?")
age=int(input("how old are you?"))
print(f"nice to meet you,{name}")
answer=input("How do you feel today?").strip().lower()
if any(word in answer for word in ["happy","good","okay","ok","fine","alright"]):
    print("It's good to hear that!")
    conv=input("Would you like a friendly conversation with me?Yes/no ").strip().lower()
    if conv=="yes":
        print("Yay!Let's have a friendly chat!")
        rating=int(input("How has your day been in a scale out of ten?"))
        if rating==0:
            print("It must have been a really tough day for you...I hope you feel better soon")
        elif rating <=4:
            print("That's a rough day...")
        elif rating <=8:
            print("That's a solid day!")
        elif rating <=10:
            print("Seems like your day has been amazing!I'm glad to hear that!")
        else:
            rate=int(input("Please type a number between 1-10"))
            if rate<=5:
                help=input("Gosh,you deserve a better day than this...I'm surprised you made it so far through the day-Can I help in any way?").strip().lower()
                if any(word in help for word in["yes","yh","yhh","yeah","yup","can you?","ig","i guess"]):
                    emotion=input("Alright then,even if I can't be present there with you,I hope I can still help.Firstly,thank you for sharing how you feel with me.I'm here to help you in any way I possibly can, I understand that you're not feeling well today and that's okay.If you can, could you please tell me how you feel right now?Do you feel upset,angry,exhausted,or is it that indescribable empty feeling?...(please pick one) ")
                    if any(word in emotion for word in["mad","angry","sad","upset","depressed"] ):
                        print("That's terrible...You must have a great reason for that.Although,I'm here to support you through your day,I strongly recommend you reach out to someone that you're comfortable having this discussion with.")
                    elif any(word in emotion for word in["exhausted","tired",]):
                        print("I'm really sorry that it was that tough..")
                    elif any(word in emotion for word in["empty","i don't know","indescribable"]):
                       print("Your feeling is usually caused by deep hidden sadness-the sadness that doesn't feel overwhelmingly painful to the point where you would cry(even if you feel like you want to) but instead it settles in your heart as a heavy burden that you seem unable to carry.From my perspective,these emotions can be caused by silent suffering and lack of excitement in your life.Imagine if I said 'find new hobbies and try new thinngs',it may sound daft and simple at first but I truly believe that exploring new hobbies and trying new things can make days feel more special!Try hobbies such as painting,drawing,learning a new instrument,gardening or any other hobby that calms your mind and allows you to enjoy it.")
                    else:
                        emotion=input("please pick one")
                        if any(word in emotion for word in["mad","angry","sad","upset","depressed"]):
                            print("That's terrible...You must have a great reason for that.Although,I'm here to support you through your day,I strongly recommend you reach out to someone that you're comfortable having this discussion with.")
                        elif any(word in emotion for word in["exhausted","tired",]):
                            print("I'm really sorry that it was that tough..")
                        elif any(word in emotion for word in["empty","i don't know","indescribable"]):
                            print("Your feeling is usually caused by deep hidden sadness-the sadness that doesn't feel overwhelmingly painful to the point where you would cry(even if you feel like you want to) but instead it settles in your heart as a heavy burden that you seem unable to carry.From my perspective,these emotions can be caused by silent suffering and lack of excitement in your life.Imagine if I said 'find new hobbies and try new thinngs',it may sound daft and simple at first but I truly believe that exploring new hobbies and trying new things can make days feel more special!Try hobbies such as painting,drawing,learning a new instrument,gardening or any other hobby that calms your mind and allows you to enjoy it.")
            elif rate>=6:
                print("That's great!")
    elif conv=="no":
        print("That's alright!Have a good day!")
    else:
        print("Sorry,please retype that")

elif any(word in answer for word in["bad","mid","exhausted","tired","bored","decent","normal","as usual","sick"]):
    print("Thanks for sharing!It's okay to feel that way")
    tired=input("Has today been tiring for you?Yes/no").strip().lower()
    if tired=="yes":
        print("Feeling tired is an output of your hardwork,it really shows that you tried!As good as it is to work hard and try to accomplish your goals,"
        "it's also important to take care of yourself in the process.")
    elif tired=="no":
        print("I'm sorry to hear that you feel that way...Is there something else that's causing you to feel that way?")
else:
    feeling=input("I'm sorry,are you alright?Yes/no").strip().lower()
    if feeling=="yes":
        print("Thank goodness,that's good to know")
    elif feeling=="no":
        print("Can I help you feel better?Yes/no")
    else:
        mood=input("Could you please retype that?I'm not sure whether you meant yes or no-")
        if mood=="yes":
            print("I'm relieved hearing that!")
        elif mood=="no":
            print("I hope you you feel better soon")