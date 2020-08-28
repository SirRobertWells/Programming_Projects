# LEARNER CODE START HERE
    frequencies = {}
    file_contents = file_contents.split()
    strl = ""

    for word in file_contents:
        strl= ''.join(ch for ch in word if ch.isalnum())
        if strl.lower() not in uninteresting_words:
            if strl.lower() not in frequencies:
                frequencies[strl.lower()] = 1
            else:
                frequencies[strl.lower()]+=1