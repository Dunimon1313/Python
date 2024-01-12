def knight_check(word):
  phrase = "UCF charge onto the field. With our spirit, we’ll never yield. Black and gold, Charge right through the line. Victory is our cry, V-I-C-T-O-R-Y. Tonight our Knights will shine!"
  lowPhrase = phrase.lower()
  word = word.lower()
  if word in lowPhrase:
    return True
  else:
    return False

wordExists = knight_check(input("Please enter a word to search for.\n"))
if(wordExists):
  print("Word found")
else:
  print("Word not found")