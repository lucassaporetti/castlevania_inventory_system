def animated_item_gif(self):
    movie = QtGui.QMovie("/home/lucassaporetti/GIT-Repository/"
                         "castlevania_inventory_system/src/resources/"
                         "images/items/alucard_sword_animation.gif")
    self.itemGifAnimation.setMovie(movie)
    movie.start()
    movie2 = QtGui.QMovie("/home/lucassaporetti/GIT-Repository/"
                          "castlevania_inventory_system/src/resources/"
                          "images/items/alucard_sword_special.gif")
    self.itemGifSpecial.setMovie(movie2)
    movie2.start()


def show_item_image(self):
    item_image = '/home/lucassaporetti/GIT-Repository/' \
                 'castlevania_inventory_system/src/' \
                 'resources/images/items/alucard_sword_icon.png'
    qimage = QtGui.QImage(item_image)
    pixmap = QtGui.QPixmap.fromImage(qimage)
    pixmap_image = QtGui.QPixmap(pixmap)
    self.itemImage.setPixmap(pixmap_image)
    self.itemImage.show()