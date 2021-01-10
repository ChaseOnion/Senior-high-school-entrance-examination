import time
def get():
    now = time.time()
    exam_time = 1623772800
    behind = exam_time - now
    day = behind / 3600 / 24
    print(f"距离杨念中考还差{int(day)}天")
get()
