from streamlit import *
from time import *

set_page_config("Tarskiy to'plamlari",'⚙️', 'wide', 'expanded')
title("Tarskiy-Kuratskiy to'plamlari (Sonning bo'luvchilarini topish dasturi)")
n=select_slider("Sonlarni kiriting", options=[i for i in range(1_0001)])

tab1,tab2 = tabs(["1-oyna Sonlarning bo'luvchilari","2-oyna Murakkab sonlar"])

start = time()
with tab1:
    with expander("Natijalar pastda", icon='🪫'):
            json([i for i in range(1,n+1) if n%i==0])
    write(sum([i for i in range(1,n+1) if n%i==0]))
    write(sum([i for i in range(1,n+1) if n%i==0])-n==n)
    end = time()-start
    vaqt = f"{end*1_000:.3f}"
    end1 = end-time()

with tab2:
    k=0
    for j in range(1,n+1):
        murakkab=sum([i for i in range(1,j+1) if j%i==0])-j
        if murakkab==j:
            k+=1
            json({
                k:j
            })

metric("Vaqt farqi", vaqt, (end1-end))