import sublime, sublime_plugin

class SaveOnModifiedListener(sublime_plugin.EventListener):
  pending = 0
  def on_modified(self, view):
      self.pending+=1
      if self.pending > 20:
          view.run_command("save")
          self.pending=0
