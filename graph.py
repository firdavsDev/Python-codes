import  pygal

chiziqli=pygal.Line()

chiziqli.title="Stastika"

chiziqli.x_labels=['Fevral','Mart','April']

chiziqli.add('Instagram',[9.25,12,5.6])

chiziqli.add('YouTube',[11.35,22,4.6])

chiziqli.render_in_browser()
