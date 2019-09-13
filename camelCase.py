
def camelcase(sentence):
    title_case = sentence.title() 
    upper_camel_cased = title_case.replace(' ', '') 
    
    return upper_camel_cased[0:1].lower() + upper_camel_cased[1:] 
	
def main():
    sentence = input('Enter your sentence: ')
    output = camelcase(sentence)
    print(output)


if __name__ == '__main__':
	main()

def display_Banner():
    """Display program bane in banner """
    msg = 'Awesome'
    stars = '*' * len(msg)
    print(f'\n {stars} \n, {msg} \n')

print('This is how you work the program')