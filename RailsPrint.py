import sublime, sublime_plugin

class RailsPrintCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		str1 = "<%=  %>"
		self.view.replace(edit, self.view.sel()[0], str1)
