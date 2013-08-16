import sublime, sublime_plugin

class InsertMynameCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		myname = "keitarou.oonishi"
		self.view.replace(edit, self.view.sel()[0], myname)
