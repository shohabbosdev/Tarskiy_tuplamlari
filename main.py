from streamlit import *
from time import *

title("Torskiy-Kuratskiy to'plamlari (Sonning bo'luvchilarini topish dasturi)")
n=select_slider("Sonlarni kiriting", options=[i for i in range(10001)])
running_time = []

start = time()
json(([i for i in range(1,n+1) if n%i==0]))
write(sum([i for i in range(1,n+1) if n%i==0]))
end = time()-start
running_time.append(end)
end1 = time()-end
end = f"{end*1_000:.2f}"
metric("Ishlash vaqti", end, running_time[-1]/end1)