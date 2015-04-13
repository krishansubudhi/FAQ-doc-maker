import pyinotify
import sys
import FAQhtmlConverter
# The watch manager stores the watches and provides operations on watches
folder = sys.argv[1]
wm = pyinotify.WatchManager()

mask = pyinotify.IN_DELETE | pyinotify.IN_CREATE | pyinotify.IN_CLOSE_NOWRITE # watched events

class EventHandler(pyinotify.ProcessEvent):
    def process_IN_CREATE(self, event):
        print "Creating:", event.pathname
        FAQhtmlConverter.make_html(folder)

    def process_IN_DELETE(self, event):
        print "Removing:", event.pathname

    def process_IN_CLOSE(self,event):
	print "closing write operation:", event.pathname

handler = EventHandler()
notifier = pyinotify.Notifier(wm, handler)
wdd = wm.add_watch(folder, mask, rec=False)
notifier.loop()
