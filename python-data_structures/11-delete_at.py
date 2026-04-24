#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    Siyahıda müəyyən edilmiş indeksdəki elementi silir.
    """
    # İndeksin mənfi və ya diapazondan kənar olub-olmadığını yoxlayırıq
    if idx < 0 or idx >= len(my_list):
        return my_list

    # del operatoru siyahıdakı elementi verilmiş indeks üzrə silir
    del my_list[idx]
    return my_list
