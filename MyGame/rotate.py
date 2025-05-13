class Rotate():
    #旋轉系統
    def rotate(self):
        d = move.choose.index(move.n)+1
        if d-len(move.choose) >= 0:
            d = d-len(move.choose)
        move.n = move.choose[d]
        move.draw()