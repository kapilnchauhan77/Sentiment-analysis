from textblob import TextBlob

def get_input():
	input_statement = input('Please provide a statement: ')
	return input_statement

a = get_input()

analyse_this = TextBlob(a)

analyse_this.correct()

b = analyse_this.sentiment.polarity
c = analyse_this.sentiment.subjectivity
print(b,c)
if b < (-0.45) :
    if c < 0.45 :
        print(' Your thoughts are negative but logical and factual')
                
    else:
        print(' Your thoughts are negative but entitled to your personal opinion')

elif b > (-0.45) and b < 0.00 :
    if c < 0.45 :
        print(' Your thoughts are just a bit negative but logical and factual')
    else:
        print(' Your thoughts are just a bit negative but entitled to your personal opinion')
elif b == 0.00 :
    if c < 0.45 :
        print(' Your thoughts are neutral but logical and factual')
    else:
        print(' Your thoughts are neutral but entitled to your personal opinion')
elif b > 0.00 and b < 0.35:
    if c < 0.45 :
        print(' Your thoughts are quite positive and logical as well as factual')
    else:
        print(' Your thoughts are quite positive but entitled to your personal opinion')
elif b > 0.35:
    if c < 0.45 :
        print(' Your thoughts are very positive and logical as well as factual')
    else:
        print(' Your thoughts are very positive but entitled to your personal opinion')