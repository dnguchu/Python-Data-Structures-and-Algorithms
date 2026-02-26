#problem 1
def greeting(language): 
    if language== 'eng': 
        return 'hello world' 
    if language  == 'fr': 
        return 'Bonjour le monde' 
    else:
        return 'language not supported' 

l = [greeting('eng'), greeting('fr'), greeting('de')]
l[2]

def callf(f):
    lang = 'eng'
    return (f(lang))

callf(greeting)