import fileinput
"""The first functions are the correction-functions that will be used to correct the .txt-file"""
def correction_space(li):
    """This function eliminates consecutive elements of the form ' ' inside a list. 
    It will be used to eliminate superflous spaces in a text file"""
    for n in range(len(li)):
        if n == len(li)-1:
            break
        elif li[n]==' ' and li[n+1]==' ':
            while li[n+1]==' ':
                del li[n]
        elif li[n]==' ' and (li[n+1]=='.' or li[n+1]==';' or li[n+1]==','):
            del li[n]        
        #the function eliminates ' ' whnever it appears before a point, a semicolon or a comma.
          
def correction_point(li,s):
    """This function takes a list and a string as arguments. The function will be called with s='.', s='!', s='?'"""

    for n in range(len(li)):
        if li[n]==s:
            if li[n+1]==' ':
                if li[n+2].islower():
                    li[n+2]=li[n+2].upper()
            #the function substitutes a lowercase letter after a space after s with its uppercase.
            else:
                if li[n+1].islower():
                    li.insert(n+1,' ')
                    li[n+2]=li[n+2].upper()
            #if there is no space after s and the following element is a lowercase letter, the function first insterts
            #a space and then substitutes the lowercase letter with its uppercase
                else:
                    li.insert(n+1,' ')
            #if there is no space after s, the functions insert a ' '.

def correction_comma(li,c):
    """This function takes a list and a string as arguments. It will be called with c=',' c=';'. The fuction insert a space
    after c if there is none"""
    for n in range(len(li)):
        if li[n]==c and li[n+1]!=' ':
            li.insert(n+1,' ')

def correct(line):
    """This function takes a string as argument and returns a list whose items are the same as the string's items. Finally the 
    correction-functions above are applied to the items of this list and the corrected string is returned"""
    li=list(line)
    correction_space(li)
    correction_point(li,'.')
    correction_point(li,'!')
    correction_point(li,'?')
    correction_comma(li,',')
    correction_comma(li,';')
    return ''.join(li)

def correct_file(file):
    """This function opens a file and replaces each line with the correct(line)"""
    for line in fileinput.input(file, inplace=True): 
        print line.replace(line, correct(line))
