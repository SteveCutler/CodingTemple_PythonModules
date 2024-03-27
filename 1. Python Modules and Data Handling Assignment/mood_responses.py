def mood_response(mood):
    var = ""
    if "happy" in mood:
        return "That's great! Glad to hear you're happy"

    elif "sad" in mood:
        return "Aw that's too bad, hope you feel better!"

    elif "depressed" in mood:
        return "Try to do something nice for yourself today!"

    elif "angry" in mood:
        return "Its ok to be angry, try channeling it in a productive way!"

    else:
       return "Make sure you include one of the valid moods in your response!"