import sublime, sublime_plugin
from datetime import date

class InsertTodayCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		v = self.view
		today = date.today()
		self.view.replace(edit, v.sel()[0], str(today))
