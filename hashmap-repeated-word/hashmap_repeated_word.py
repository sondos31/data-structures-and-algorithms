import re
from Linked_List.linked_list.Linked_list import LinkedList

def repeated_word(string):
    """
    method finds the first word to occur more than once in a string.
    :param string:
    :return: string
    """
    list = LinkedList()
    words = re.sub(",", "", string)
    words =words.split(' ')
    print(words)
    for i in words:
        i = i.lower()
        if list.includes(i):
            return i
        else:
            list.insert(i)
    return None


print(repeated_word("Once upon a time"))
print(repeated_word("It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York..."))
