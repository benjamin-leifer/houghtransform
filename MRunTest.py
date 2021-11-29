import MaccorRunFileGenerator as Maccor
import time

generator = Maccor.MaccorRunFileGenerator()
generator.selectWorkbookSheet()
generator.root.mainloop()
time.sleep(20)