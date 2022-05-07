import inkex

# Based on the Inkscape extension "Export to PNG" - https://gitlab.com/inkscape/extensions

# Define an Inkscape extension for exporting the image to a .ico file
class IcoOutput(inkex.RasterOutputExtension):

	def add_arguments(self, pars):
		pars.add_argument("--tab")
		pars.add_argument('--size', type=int, default=32, help='Icon Size')

	def save(self, stream):
		self.img.convert("RGBA").save(stream, format = 'ICO', sizes=[(self.options.size, self.options.size)]) #sizes=[(16,16), (24,24), (32,32), (48,48), (64,64), (96,96), (128,128), (256,256)])

if __name__ == '__main__':
	IcoOutput().run()