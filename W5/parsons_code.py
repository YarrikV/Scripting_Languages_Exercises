def maximum_deviation(code):
    """
    >>> maximum_deviation('*RUURDDDDRUURDR')
    (-2, 2)
    >>> maximum_deviation('*uduududdduu')
    (-1, 2)
    >>> maximum_deviation('*DRRUUDDRUURDUDURDDU')
    (-1, 1)
    """
    deviation = [0]
    for char in code[1:].upper():
        if char == "R":
            deviation.append(deviation[-1])
        elif char == "U":
            deviation.append(deviation[-1] + 1)
        elif char == "D":
            deviation.append(deviation[-1] - 1)
        else:
            raise ValueError(f"Invalid movement character: {char}")
    return min(deviation), max(deviation)


def parsons(filename):
    """
    >>> parsons('parsons_01.txt')
    '*RUURDDDDRUURDR'
    >>> parsons('parsons_02.txt')
    '*UDUUDUDDDUU'
    >>> parsons('parsons_03.txt')
    '*DRRUUDDRUURDUDURDDU'
    """
    code = [[]]
    with open(filename, "r") as f:
        for line in f:
            base = 0
            if code[-1]:
                code.append([])
            while (idx := line.find("*")) >= 0:
                code[-1].append(base + idx)
                line = line[idx+2:]
                base += idx+2
            code[-1] = [h // 2 for h in code[-1]]

    length = sum(len(line) for line in code)
    code_str = ""
    base = None
    for i in range(length):
        for line_idx, line in enumerate(code):
            if i in line:
                if base is None:
                    assert len(code_str) == 0
                    code_str += "*"
                else:
                    diff = base - line_idx
                    if diff == 1:
                        code_str += "U"
                    elif diff == 0:
                        code_str += "R"
                    elif diff == -1:
                        code_str += "D"
                    else:
                        raise ValueError(f"Deviation of {diff} is too extreme (-1,0,1).")
                base = line_idx
    return code_str


def amount_of_lines_parson(max_dev, min_dev):
    """
    >>> amount_of_lines_parson(2, -2)
    9
    >>> amount_of_lines_parson(2, -1)
    7
    >>> amount_of_lines_parson(1, -1)
    5
    """
    return (max_dev - min_dev)*2 + 1


def add_to_contour(list_of_strings, idx, char="*"):
    """Adds char to list_of_strings[idx].
    Adds " " on other strings in the list."""
    list_of_strings = [(line+char if line_idx == idx % len(list_of_strings) else line+" ") for line_idx, line in enumerate(list_of_strings)]
    return list_of_strings


def contour(code, filename=None):
    """
    >>> contour('*RUURDDDDRUURDR')
          *-*                    
         /   \                   
        *     *                  
       /       \                 
    *-*         *         *-*    
                 \       /   \   
                  *     *     *-*
                   \   /         
                    *-*           
    >>> contour('*RUURDDDDRUURDR', 'contour_01.txt')

    >>> contour('*uduududdduu')
            *   *          
           / \ / \         
      *   *   *   *       *
     / \ /         \     / 
    *   *           *   *  
                     \ /   
                      *    
    >>> contour('*uduududdduu', 'contour_02.txt')

    >>> contour('*DRRUUDDRUURDUDURDDU')
              *         *-*   *   *-*      
             / \       /   \ / \ /   \     
    *       *   *     *     *   *     *   *
     \     /     \   /                 \ / 
      *-*-*       *-*                   *  
    >>> contour('*DRRUUDDRUURDUDURDDU', 'contour_03.txt')
    """
    code = code.upper()
    diff_dict = {
            "U":(1, "/"), "D":(-1, "\\"), "R":(0, "-"), "*": (None,None)
    }

    # nr of diff pitches
    mini, maxi = maximum_deviation(code)
    size = amount_of_lines_parson(maxi, mini)

    contour_list = ["" for _ in range(size)]
    
    # these idx are without x2 factor
    previous_idx = None
    this_idx = None

    for char in code:
        # find line where "*" should be 
        diff_idx, diff_char = diff_dict[char]

        if diff_char is None:
            this_idx = - mini
        else:
            this_idx = previous_idx + diff_idx
        
        # don't forget x2 factor to idx
        if previous_idx is not None:
            contour_list = add_to_contour(contour_list, previous_idx*2+diff_idx, char=diff_char)
        contour_list = add_to_contour(contour_list, this_idx*2)
        
        previous_idx = this_idx

    if not filename:
        # contour
        for line in contour_list[::-1]:
            print(line)
    else:
        with open(filename, "w") as f:
            for line in contour_list[::-1]:
                f.write(line+"\n")


if __name__ == "__main__":
    import doctest

    doctest.testmod()
