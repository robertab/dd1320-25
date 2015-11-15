from Song import Song


def readfile(the_file):
    pass


def linsok(the_list, artistname):
    for obj in (range(len(the_list))):
        if the_list[obj].artist == artistname:
            return True


def sortera(data):
    if len(data) > 1:
        mitten = len(data)//2
        vensterHalva = data[:mitten]
        hogerHalva = data[mitten:]

        sortera(vensterHalva)
        sortera(hogerHalva)

        i, j, k = 0, 0, 0
    
        while i < len(vensterHalva) and j < len(hogerHalva):
            if vensterHalva[i] < hogerHalva[j]:
                data[k] = vensterHalva[i]
                i = i + 1
            else:
                data[k] = hogerHalva[j]
                j = j + 1
            k = k + 1
                
        while i < len(vensterHalva):
            data[k] = vensterHalva[i]
            i = i + 1
            k = k + 1
                    
        while j < len(hogerHalva):
            data[k] = hogerHalva[j]
            j = j + 1
            k = k + 1
    return data


def binsok(the_list, artist):
    if len(the_list) == 0:
        return False

    else:
        mid = len(the_list)//2
        if artist == the_list[mid].get_artist():
            return True

        else:

            if artist < the_list[mid].get_artist():
                return binsok(the_list[:mid], artist)

            else:
                return binsok(the_list[mid:], artist)


