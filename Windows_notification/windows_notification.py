import time
from winotify import Notification, audio

toast = Notification(app_id="NeuralNine Script",
                    title="Important Info",
                    msg="Learn Python & Machine Learning",
                    duration="long",
                    icon=r"C:\Users\mhzei\Documents\GitHub\PythonSmallProjects\Windows_notification\neural.png")

toast.add_actions(label="Click Me", launch="https://neuralnine.com/")
toast.add_actions(label="YouTube", launch="https://www.youtube.com/channel/UC8wZnXYK_CGKlBcZp-GxYPA")

toast.set_audio(audio.LoopingAlarm, loop=True)



toast.show() 