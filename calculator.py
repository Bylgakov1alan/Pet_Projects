import re



theInputString = '++++----)(((////)-+++///2343-*sadfadfb r///fda(%+/++/%/%/%)_()+!!!***--)))7++++++----sdfsdf65' #input()

lenNewString = len(theInputString)


numbers = "0123456789"
operators = "().+-/%*"

if numbers in theInputString:
    print ("да цифры есть")
    if operators in theInputString:
        print("да есть операторы")
        
russianLetters = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
englishLetters = "abcdefghijklmnopqrstuvwxyz"
spechSimvol = '!"#$&\' ,:;<=>?@[\\]^_`{|}~'
spechsymvol =0
lineWithoutAdditionalCharacters = ""


        
for i in range(0,lenNewString):
    if theInputString[i] in numbers or theInputString[i] in operators:
        spechsymvol += 1
        lineWithoutAdditionalCharacters = lineWithoutAdditionalCharacters + theInputString[i]
    else:
        spechsymvol += 1
# lineWithoutAdditionalCharacters = 3()()+)))7

theFirstOccurrence = re.search(r'\d', lineWithoutAdditionalCharacters).start()

indexSkobok = ""
kol_vo_SkobokOtkr = 0
kol_vo_SkobokZakr = 0

for i in range(0,theFirstOccurrence):
    if lineWithoutAdditionalCharacters[i] == '(':
        kol_vo_SkobokOtkr += 1
        indexSkobok = indexSkobok + f"тут есть скобка {lineWithoutAdditionalCharacters[i]} под таким индексом {i} \n"
    elif lineWithoutAdditionalCharacters[i] == ')':
        kol_vo_SkobokZakr += 1
        indexSkobok = indexSkobok + f"тут есть скобка {lineWithoutAdditionalCharacters[i]} под таким индексом {i} \n"
        
        
print(kol_vo_SkobokOtkr,kol_vo_SkobokZakr)

if kol_vo_SkobokOtkr>kol_vo_SkobokZakr:
    NewString = "(" + lineWithoutAdditionalCharacters[theFirstOccurrence:len(lineWithoutAdditionalCharacters)]
else:
    NewString = lineWithoutAdditionalCharacters[theFirstOccurrence:]
    
    
print(NewString)
print(indexSkobok)

indexSkobok=""
kol_vo_SkobokOtkr=0
kol_vo_SkobokZakr=0

print("разделитель")

for i in range(0,len(NewString)):
    if NewString[i] == '(':
        kol_vo_SkobokOtkr += 1
        indexSkobok = indexSkobok + f"тут есть скобка {NewString[i]} под таким индексом {i} \n"
    elif NewString[i] == ')':
        kol_vo_SkobokZakr += 1
        indexSkobok = indexSkobok + f"тут есть скобка {NewString[i]} под таким индексом {i} \n"

print(indexSkobok)

def PoiskNenyznyxSkobok(String):
    for i in range(0,len(String)-1):
        if String[i] == "(" and String[i+1] == ")":
            NewString1 = String[:i] + String[i+2:]
    if "()" in NewString1:
          NewString1=PoiskNenyznyxSkobok(NewString1)
    return NewString1

print (PoiskNenyznyxSkobok(NewString))
NewString = PoiskNenyznyxSkobok(NewString)

def PoiskPoftorSkobok(String):
    for i in range(0,len(String)-1):
        if (String[i] == "(" and String[i+1] == "(") or (String[i] == ")" and String[i+1] == ")"):
            NewString1 = String[:i] + String[i+1:]
    if "((" in NewString1 or "))" in NewString1:
          NewString1=PoiskPoftorSkobok(NewString1)
    return NewString1

print(PoiskPoftorSkobok(NewString))
NewString = PoiskPoftorSkobok(NewString)

def SearchReturnedOperators(String):
    for i in range(0,len(String)-1):
        if (String[i] == "+" and String[i+1] == "+") or (String[i] == "-" and String[i+1] == "-") or (String[i] == "*" and String[i+1] == "*") or (String[i] == "/" and String[i+1] == "/") or (String[i] == "%" and String[i+1] == "%"):
            NewString1 = String[:i] + String[i+1:]
    if "++" in NewString1 or "--" in NewString1 or "//" in NewString1 or "%%" in NewString1 or "**" in NewString1:
          NewString1=SearchReturnedOperators(NewString1)
    return NewString1

print(SearchReturnedOperators(NewString))
    
NewString=SearchReturnedOperators(NewString)
    
    
def PoiskOneNumber(NewString):
    OneNumber  = re.search(r'\d+', NewString)
    return OneNumber


def PoiskTwoNumber(NewString):
    OneNumber = PoiskOneNumber(NewString) 
    TwoNumber = re.search(r'\d+', NewString[int(OneNumber.end())+1:])
    return TwoNumber
    
    
def ChetPervoyPary(NewString):
    OneNumber = PoiskOneNumber(NewString).group()
    TwoNumber = PoiskTwoNumber(NewString).group()
    
    IndexEndOneNumbers = PoiskOneNumber(NewString).end()
    IndexStartTwoNumbers = PoiskTwoNumber(NewString).start()
    print(IndexEndOneNumbers, IndexStartTwoNumbers)
    
    for i in range(IndexEndOneNumbers,IndexStartTwoNumbers):
        if NewString[i] == "/":
            print(OneNumber,"/",TwoNumber,"=",int(OneNumber)/int(TwoNumber))
            OneOperatorCounted = f"{OneNumber}/{TwoNumber}"
            break
        elif NewString[i] == "%":
            print(OneNumber,"%",TwoNumber,"=",int(OneNumber)%int(TwoNumber))
            OneOperatorCounted = f"{OneNumber}%{TwoNumber}"
            break
        elif NewString[i] == "*":
            print(OneNumber,"*",TwoNumber,"=",int(OneNumber)*int(TwoNumber))
            OneOperatorCounted = f"{OneNumber}*{TwoNumber}"
            break
        elif NewString[i] == "-":
            print(OneNumber,"-",TwoNumber,"=",int(OneNumber)-int(TwoNumber))
            OneOperatorCounted = f"{OneNumber}-{TwoNumber}"
            break
        elif NewString[i] == "+":
            print(OneNumber,"+",TwoNumber,"=",int(OneNumber)+int(TwoNumber))
            OneOperatorCounted = f"{OneNumber}+{TwoNumber}"
            break
        # OneOperatorCounted = OneOperatorCounted + str(NewString[int(IndexStartTwoNumbers)+int(IndexEndOneNumbers)-1:len(NewString)])
    return OneOperatorCounted

NewStringPerIterachiya = ChetPervoyPary(NewString)

def ProverkaSkobok(NewString, NewStringPerIterachiya):
    OneNumber = PoiskOneNumber(NewString).group()
    TwoNumber = PoiskTwoNumber(NewString).group()
    
    IndexEndOneNumbers = PoiskOneNumber(NewString).end()
    IndexStartTwoNumbers = PoiskTwoNumber(NewString).start()
    Skoboka_Otkr_Interval_Nach_PervChifra, Skoboka_Zakr_Interval_Nach_PervChifra = 0,0
    flag_pered_pervoy_chifroy=0
    Skoboka_Otkr_Interval_One_AND_Two, Skoboka_Otkr_Interval_Nach_PervChifra, flag_pered_pervoy_chifroy = 0,0,0
    
    for i in range(0,IndexEndOneNumbers):
        if NewString[i]=="(":
            Skoboka_Otkr_Interval_Nach_PervChifra=Skoboka_Otkr_Interval_Nach_PervChifra+1
            print("есть скобочка (")
        if NewString[i]==")":
            Skoboka_Zakr_Interval_Nach_PervChifra=Skoboka_Zakr_Interval_Nach_PervChifra+1
            print("есть скобочка (")
            
    if Skoboka_Otkr_Interval_Nach_PervChifra == Skoboka_Zakr_Interval_Nach_PervChifra:
        print("ничего не нужно")
    elif Skoboka_Otkr_Interval_Nach_PervChifra < Skoboka_Zakr_Interval_Nach_PervChifra:
        print("ничего не нужно")
    elif Skoboka_Otkr_Interval_Nach_PervChifra > Skoboka_Zakr_Interval_Nach_PervChifra:
        flag_pered_pervoy_chifroy=1
        print("нужны скобки перед выражением")
        
    for i in range(IndexEndOneNumbers,IndexStartTwoNumbers):
        if NewString[i]=="(":
            Skoboka_Otkr_Interval_One_AND_Two=Skoboka_Otkr_Interval_One_AND_Two+1
            print("есть скобочка (")
        if NewString[i]==")":
            Skoboka_Zakr_Interval_One_AND_Two=Skoboka_Zakr_Interval_One_AND_Two+1
            print("есть скобочка (")
    
    if Skoboka_Otkr_Interval_Nach_PervChifra == Skoboka_Zakr_Interval_Nach_PervChifra:
        print("ничего не нужно")
    elif Skoboka_Otkr_Interval_Nach_PervChifra < Skoboka_Zakr_Interval_Nach_PervChifra:
        print("ничего не нужно")
    elif Skoboka_Otkr_Interval_Nach_PervChifra > Skoboka_Zakr_Interval_Nach_PervChifra:
        flag_pered_pervoy_chifroy=1
        print("нужны скобки в середине выражения выражением")        
    
            
    # for i in range(IndexEndOneNumbers, len(NewString)):
    #         if NewString[i]==")":
    #             Skobok_Interval_Nach_PervChifra+=1
    #             print("есть скобочка )")

ProverkaSkobok(NewString, NewStringPerIterachiya)
print(NewString)
print(NewStringPerIterachiya)


