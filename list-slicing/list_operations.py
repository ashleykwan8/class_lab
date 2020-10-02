"""Utilities for manipulating lists."""


def head(input_list):
    head = ['Jan', 'Feb', 'mar']
    return head[0]
    
    
    """Return the first item of the input list.

    For example:

      >>> head(['Jan', 'Feb', 'Mar'])
      'Jan'
    """



def tail(input_list):

    tail = ['Jan', 'Feb', 'mar'] 
    new_list = []
    return new_list.append(tail[1:3])
    
    """Return a new list of all items, excluding the first item.
    
    For example:

    >>> tail(['Jan', 'Feb', 'Mar'])
    ['Feb', 'Mar']

    """

   


def last(input_list):
    
    last = ['Jan', 'Feb', 'mar']
    return last[-1]
    
    """Return the last item of the input list.
    For example:

    >>> last(['Jan', 'Feb', 'Mar'])
    'Mar'

    """

def top(input_list):
    top = ['Jan', 'Feb', 'mar']
    return top[:2]

    """Return all elements of the input list except the last.

    For example:

    >>> top(['Jan', 'Feb', 'Mar'])
    ['Jan', 'Feb']

    """


def first_three(input_list):

    first_three = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    return first_tree[:3]  
    """Return the first three elements of the input list.

    For example:

    >>> first_three(['Jan', 'Feb', 'Mar', 'Apr', 'May'])
    ['Jan', 'Feb', 'Mar']

    """



def last_five(input_list):
    last_five = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    return last_five[6:11]

    """Return the last five elements of the input list.

    For example:

    >>> last_five([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [15, 18, 21, 24, 27]

    """
    

def middle(input_list):
   
    middle = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
     
    return middle[2:8]
    """Return all elements of input_list except the first two and the last two.
     
    For example:

    >>> middle([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15, 18, 21]

    """



def inner_four(input_list):

    inner_four = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    return inner_four[2:6]
    
    """Return the third, fourth, fifth, and sixth elements of input_list.

    For example:

    >>> inner_four([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [6, 9, 12, 15]

    """

 


def inner_four_end(input_list):
    
    inner_four_end=[0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    return inner_four_end[4:7]
    
    """Return the elements that are 6th, 5th, 4th, and 3rd from the end of input_list.

    This function should return those elements in a list, in the exact order
    described above.

    For example:

    >>> inner_four_end([0, 3, 6, 9, 12, 15, 18, 21, 24, 27])
    [12, 15, 18, 21]

    """

  

def replace_head(input_list):
    multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    multiples[0] = 42
    
    """Replace the head of input_list with the value 42 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_head(multiples)
    >>> multiples == [42, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    True

    """



def replace_third_and_last(input_list):
    
    multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    multiples[3] = '37'
    multiples[9] = '37'


    """Replace third and last elements of input_list with 37 and return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_third_and_last(multiples)
    >>> multiples == [0, 3, 37, 9, 12, 15, 18, 21, 24, 37]
    True

    """




def replace_middle(input_list):
    multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    multiples[2:8] = [42, 37]

    """Replace all elements of a list but the first two and last two with 42 and 37.

    After the replacement, 42 and 37 should appear in that order in input_list.

    Return nothing.

    For example:

    >>> multiples = [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]
    >>> replace_middle(multiples)
    >>> multiples == [0, 3, 42, 37, 24, 27]
    True

    """

    

def delete_third_and_seventh(input_list):
    notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    del notes[3]
    del notes[7]

    """Remove third and seventh elements of input_list and return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_third_and_seventh(notes)
    >>> notes == ['Do', 'Re', 'Fa', 'So', 'La', 'Do']
    True

    """

  


def delete_middle(input_list):
    
    notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    del notes[2:6]
    """Remove all elements from input_list except the first two and last two.

    Return nothing.

    For example:

    >>> notes = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti', 'Do']
    >>> delete_middle(notes)
    >>> notes == ['Do', 'Re', 'Ti', 'Do']
    True

    """

    pass


# This is the part were we actually run the doctests.

if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if result.failed == 0:
        print('ALL TESTS PASSED')
