# write a python program to translate the message into secret code language. use the rules below to translate normal english into secret code language.

# coding:
# if the the word contains atleast 3 characters, remove the first letter and append it to the end now spend three random characters at the starting and the end

# else :
# sinmply reverse the string 

# decoding:
# # if the word contains less 3 characters, reverse it 

# else 
# remove random 3 characters from start and end. now remove last letter and append it at the end now spend three random characters at the starting and the end

# else:
# simply reverse the string

# decoding:
# if the word contains less 3 characters, reverse it
st = input("Enter the message: ")
words = st.split()
coding = True
if(coding):
    nwords = []
    for word in words:
        if len(word) >= 3:
            word = word[1:] + word[0]
            nwords.append(word)
        else:
            word = word[::-1]
            nwords.append(word)
            print(" ".join(nwords))
