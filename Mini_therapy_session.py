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
                            print("The sadness that doesn't feel overwhelmingly painful to the point where you would cry(even if you feel like you want to) but instead it settles in your heart as a heavy burden that you seem unable to carry.")
                            end=input("Before we end our conversation,is there anything else you woould like to share with me?")
                            print("Oh-I understand,please make sure to take care of yourself more often.")
                elif any(word in help for word in["no","nah","nope","not really","you can't"]):
                    print("Oh well,I'mm sorry that I can't help you,I hope you have a good day though.Take care!")
                else:
                    agree=input("Was that a yes?")
                    if agree=="yes":
                        quote=input("Would you like me to find you a few great quotes I think you'll like?Yes/no").stip().lower()
                        if quote=="yes":
                            print("Remember:Let your smile change the world,don't let the world change your smile!")
                        else:
                            print("No worries!")
                    elif agree=="no":
                        print("Have a good day then!")

            elif rate>=6:
                print("That's great!")
    elif conv=="no":
        print("That's alright!Have a good day!")
    else:
        correction=input("Sorry,please retype that")
        if correction=="yes":
            print("Sure,")

elif any(word in answer for word in["bad","mid","exhausted","tired","bored","decent","normal","as usual","sick"]):
    print("Thanks for sharing!It's okay to feel that way")
    tired=input("Has today been tiring for you?Yes/no").strip().lower()
    if tired=="yes":
        print("Feeling tired can be considered an output of your hardwork,it really shows that you tried!As good as it is to work hard and try to accomplish your goals,"
        "it's also important to take care of yourself in the process.")
    elif tired=="no":
        print("That's alright too!")
        cheer=input("Would you like me to find you a quote of affirmation?Yes/no").strip().lower()
        if cheer=="yes":
            print("Remember:we were born to be real,not to be perfect-no one is perfect,that applies both too you and me...")
        elif cheer=="no":
            print("That's alright!Take care.")
        else:
            continuation=input("Sorry,I'm not sure whether you meant a yes or a no,would youu still like to continue our conversation?Yes/no").strip().lower()
            if continuation=="yes":
                day=input("I would love to continue our conversation!How has your day been do far?Good/mid/bad?").strip().lower()
                if day=="good":
                    print("That's nice to hear!I hope your day continues well.")
                elif day=="mid":
                    print("Not too good and not too bad?I hope your day brightens as it goes by though!")
                elif day=="bad":
                    print("Oh.That sounds really hard.It's okay to have bad day;tommorow's a new start")
            if continuation=="no":
                print("Alright,goodbye!")
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