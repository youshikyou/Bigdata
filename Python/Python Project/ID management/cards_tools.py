card_list=[]

def menu_interface():

    print("*"*50)
    print("welcome to use the ID card management")
    print("")
    print("1.new")
    print("2.show")
    print("3.search")
    print("")
    print("0.quit")
    print("*"*50)

def add_ID():

    print("-"*50)
    print("add new ID ")
    new_ID={}
    new_ID['name'] = input("name: ")
    new_ID['phone'] = input("phone: ")
    card_list.append(new_ID)
    print("%s add completion!" %new_ID["name"])



def show_all():

    print("-"*50)
    print("show all IDs")

    if len(card_list)==0:

        print("no ID yet, please add new ID")
        return

    for title in ["name","phone"]:
        print(title,end="\t\t")
    print("")
    print("="*50)
    for id in card_list:
        print("%s\t\t%s"%(id["name"],id["phone"]))


def search_ID():
    print("-"*50)
    print("seach ID")
    id_name=input("please enter a search name: ")
    for id in card_list:

        if id['name']==id_name:
            for title in ["name","phone"]:
                print(title,end="\t\t")

            print("")
            print("=" * 50)
            print("%s\t\t%s" %(id["name"],id["phone"]))
            deal(id)
            break
    else:
        print("no such ID name %s" %id_name)

def deal(dict_id):
    """
    deal the found id
    """
    action=input("action to ID: [1]: modify/[2]: delete/ [0]: return: ")
    if action=="1":

        for key in dict_id:
            dict_id[key]=input_card_info(key,dict_id[key])

        print("modify id completion")

    elif action=="2":

        print("delete id")
        card_list.remove(dict_id)

    else:
        return

    print(dict_id)

def input_card_info(key,value):
    """
    input card information
    key:dict key to show the modify item
    value:dict orignal value
    return users input if there is input otherwise return value
    """
    str=input("please enter %s: " %key)
    if len(str)==0:
        return value
    else:
        return str
