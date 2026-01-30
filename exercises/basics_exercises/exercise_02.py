sentence = "Very, very, very, very tired people very rarely"
print("Real sentence: \n"+sentence+"\n")
word = input("Enter word to count: ")
print("Number of times the word "+word+" appears in the sentence: "
+str(sentence.lower().count(word.lower())))
