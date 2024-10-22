sizebig: float = 1.44
sinb = 25
strok = 50
lists = 100
kol_vo1book = sinb*strok*lists
size1book = kol_vo1book*4
for_perevod = 1024
sizemb: float = size1book/for_perevod/for_perevod
kolvo: float = sizebig / sizemb
import math
print("Количество книг, помещающихся на дискету:", math.floor(kolvo))