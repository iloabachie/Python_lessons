

import ConsolePrint.printing as cp
import ConsolePrint.console2file as c2f
import ConsolePrint.loading as cl

# c2f.startConsoleSave()

cp.printing("hello this should print letter by letter")

cp.flashprint("hello this should print letter by letter")
cp.flashtext("hello this  print letter by letter", "should", index=12)
cp.animate1("hello this should print letter by letter")
cp.animate2("hello this should print letter by letter")

# c2f.endConsoleSave()

cl.countdown(5)
# cl.loading1(10, "complete")



import animation
import time

# 1 use as class
wait_animation = animation.Wait()
wait_animation.start()
print("hello")
wait_animation.end()

#2 use as decorator
@animation.wait()
def do_something_else():
    # long function
    print("me and me")
    time.sleep(5)