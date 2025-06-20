# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word=word.lower()


    def match(self,wordcompared):
        sorted_word=sorted(self.word)

        matches=[]
        for character in wordcompared:
            if character.lower()!=self.word and sorted(character.lower())==sorted_word:
                matches.append(character)

        return (matches)
    


sadam=Anagram("listen")
print(sadam.match(["sadam","adams" "inlets"]))

    

        
