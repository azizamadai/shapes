from graphics import*

bTriWin = GraphWin("Blue Triangle!", 600, 600)
bTriWin.setCoords(0, 0, 600, 600)

bTri = Polygon (Point(30, 30), Point(90, 90), Point(210,30))
bTri.setFill(color_rgb(132, 112, 255))
bTri.draw(bTriWin)

bTri = Polygon (Point(570, 530), Point(530, 510), Point(510,570), Point(540, 540))
bTri.setFill(color_rgb(64, 224, 208))
bTri.draw(bTriWin)

bTri = Polygon (Point(30, 570), Point(30, 500), Point(110, 500), Point(110, 570))
bTri.setFill(color_rgb(250, 128, 114))
bTri.draw(bTriWin)

bTri = Polygon (Point(570, 30), Point(530, 90), Point(510, 80), Point(510, 60))
bTri.setFill(color_rgb(255, 20, 147))
bTri.draw(bTriWin)

bTri = Polygon (Point(200, 300), Point(300, 400), Point(400, 300), Point(300, 200))
bTri.setFill(color_rgb(100, 149, 237))
bTri.draw(bTriWin)

bTriWin.getMouse()
bTriWin.close()
