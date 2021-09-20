import talk.service as tk
import talk.console as cmd

#Startup
# print(tk)
# print(cmd)

t = tk.TalkingService()
t.addTalkingSystem(cmd.Console())
t.talk("Hi I'm Alice! I'm alive!")