"""
Kurs: DD1320/25 Tillämpad datalogi med Etik
Författare: Robert Åbert, Sara Ervik, CDATE_2.
Uppgift: Lab5.1
"""

from Song import Song

def readfile(the_file):
    object_list = []
    object_dict = {}

    with open(the_file, encoding="utf8") as track_file:
        rows = track_file.readlines()

        for row in rows:
            obj = row.strip().split("<SEP>")
            object_list.append(Song(obj[0], obj[1], obj[2], obj[3]))
            object_dict[obj[2]] = object_list[len(object_list)-1]

    return object_list, object_dict

def linsok(the_list, artistname):
    found = False

    for obj in the_list:
        if obj.artist == artistname:
            found = True

    return found

def sortera(the_list):

    if len(the_list) > 1:

        mid = len(the_list)//2
        left_list = the_list[:mid]
        right_list = the_list[mid:]

        sortera(left_list)
        sortera(right_list)

        i, j, k = 0, 0, 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] < right_list[j]:
                the_list[k] = left_list[i]
                i = i+1

            else:
                the_list[k] = right_list[j]
                j = j+1
            k = k+1

        while i < len(left_list):
            the_list[k] = left_list[i]
            i = i+1
            k = k+1
        
        while j < len(right_list):
            the_list[k] = right_list[j]
            j = j+1
            k = k+1

    return the_list

def binsok(the_list, artistname):
    first = 0
    last = len(the_list)-1
    found = False

    while first <= last and not found:
        mid = (first + last) // 2

        if the_list[mid] == artistname:
            found = True
        else:
            if artistname < the_list[mid].get_artist():
                last = mid-1
            else:
                first = mid+1

    return found
