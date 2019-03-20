# 4.7.2. Keyword Argument
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if yo put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "I")

parrot(1000)                                            # 1 positional argument
parrot(voltage=1000)                                    # 1 keyword Argument
parrot(voltage=1000000, action='VOOOOOOM')              # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')           # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')    # 1 positional, 1 keyword

# invalid
parrot()                      # required argument missing
parrot(voltage=5.0, 'dead')   # non-keyword argument after a keyword argument
parrot(110, voltage=220)        # duplicate value for the same Argument
parrot(actor='John Cleese')     # unknown keyword argument

def function(a):
    pass

function(0, a=0)

def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop(
    "Limburger", "It's very runny, sir.",
    "It's reay very, VERY runny, sir.",
    shopkeeper="Michael Palin",
    client="John Cleese",
    sketch="Cheese Shop Sketch"
)
