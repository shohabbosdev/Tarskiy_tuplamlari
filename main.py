from streamlit import *
from time import *

set_page_config("Tarskiy to'plamlari",'⚙️', 'wide', 'expanded')
title("Tarskiy-Kuratskiy to'plamlari (Sonning bo'luvchilarini topish dasturi)")
n=select_slider("Sonlarni kiriting", options=[i for i in range(10_001)])
start = time()
with expander("Natijalar pastda", icon='🪫'):
        json([i for i in range(1,n+1) if n%i==0])
end = time()-start
write(f"Ishlash vaqti: {end*1_000:.3f} millisekund")