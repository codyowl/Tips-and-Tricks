from jinja2 import Environment, PackageLoader

package_path = PackageLoader('folder.subfolder', 'templates')
env = Environment(loader=package_path)

HTML_TEMPLATE = "yourfile.html"

final_template = env.get_template(HTML_TEMPLATE)

class Demo(object):
	def demo_function(self, first_value, second_value):
		self.first_value = first_value
		self.second_value = second_value
		self.zipped = zip(self.first_value, self.second_value) #Use zip to pack values
		self.final_template = final_template
		self.template_render = self.final_template.render(variable=self).encode('utf-8')

		 
#Inside your template:

#{% for value1, value2 in varialbe.zipped %}

#{{ value1 }} and {{ value2 }}
