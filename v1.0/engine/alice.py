import listen.service as ls
import move.service as mv
import stats.service as st
import talk.service as tk
import watch.service as wt

class Alice : 

    def __init__(self):
        print("Alice has born.")
        self.talk = tk.Service();
        self.move = mv.Service();
        self.listen = ls.Service();
        self.watch = mv.Service();
        self.stats = st.Service();


ally = Alice();


