import re
def linearize(eq:str):

    [partA, partB] = eq.split(' = ')
    var , sign = (detectX(partB))
    if(sign=="-"):
        partB=partB.replace(f'-{var}',var)
    else:
        partB=partB.replace(f'+{var}',f"-{var}")
    return f"{partA} -({partB})"



def detectX(eq):

    # Tribute to ChatGPT
    match = re.search(r'([+-]?)\s*([a-zA-Z])', eq)
    
    if match:
        sign = match.group(1) if match.group(1) else '+'
        variable = match.group(2)
        return variable, sign
    else:
        return None, None
    

def solve(eq):
    partA =linearize(eq)
   
    variable, sign = detectX(partA)
   
    result = eval(partA.replace(variable,'0'))

    res=result if sign=='-' else -1*result

    print(f"{variable} = {res}")


with open('in.txt','r') as file:
    for line in file:
        solve(line)


