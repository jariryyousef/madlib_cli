import re 
def welcome_msg():
    print("welcome to the game, guess the answer")
welcome_msg()
# to open and read file come from "dark_and_stormy_night_template" file
def read_template(pathOfFile):
    try :
        with open(pathOfFile)as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError("file not found")
    # except AssertionError :
    #     return("asseert")
  

# two arg
def parse_template(content):
    parse= re.findall(r'\{(.*?)\}', content)
    # while x
    for x in parse:    
        # Adjective
        content=content.replace((x),'',2)


        
    return content, tuple(parse)


def merge(content,parse):
    updated=content.format(*parse)

    with open('assets/test7_merge.txt','w') as result:
        result.write(updated)
    return updated

def write_new_file(content: str):
    with open('assets/dark_and_stormy_night_template_results.txt', 'w') as f:
        f.write(content)

if __name__ == "__main__":

    print("Welcome to Madlib Game")
    print("lets start the game with adding some words:")
    
    word = []
    text = read_template("assets/dark_and_stormy_night_template.txt")
    text, elemnt = parse_template(text)
    print(text)
    print(text)
    print(elemnt)

    for i in range(0, len(elemnt)):
        inp = input('enter a word  ')
        word.append(inp)
    
    word = tuple(word)
    Text = merge(text, word)
    print(Text)
    write_new_file(Text)