import os

class pages:

	def create(self,fname):
		
		#Initiate html file
		if(os.path.isfile(fname + ".html")):
			os.remove(fname + ".html")
	
		self.fhtml = open(fname + ".html",'w')
		
		#Add the Header
		with open("head.html",'r') as f:
			self.fhtml.write(f.read())
			
		#Add the navigation bar
		self.fhtml.write("<nav>")
		self.addMd(fname + "_nav.md")
		self.fhtml.write("</nav>")
		
		#Start body section
		self.fhtml.write("<div id='section-wrap'>")
		
		#Add (Left) side section
		self.fhtml.write("<aside>")
		self.addMd("aside.md")
		self.fhtml.write("</aside>")
		
		#Add main (right)  section
		self.fhtml.write("<section>")
		self.addMd(fname + "_section.md")
		self.fhtml.write("</section>")
		
		#Close body section
		self.fhtml.write("</div>")	
		
		#Add the footer
		with open("foot.html",'r') as f:
			self.fhtml.write(f.read())
		
		self.fhtml.close()
	
	def addMd(self,name):
		os.system("pandoc "+ name + " -o tmp.html")	
		with open('tmp.html','r') as f:
			self.fhtml.write(f.read())
		os.remove('tmp.html')		

		
mypages = pages()
mypages.create('index')
mypages.create('research')
