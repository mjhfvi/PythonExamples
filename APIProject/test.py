from progress.bar import Bar
import time

bar = Bar('Processing', max=100)
for i in range(100):
    time.sleep(0.01)
    bar.next()
bar.finish()
