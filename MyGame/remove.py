class Break():
    def init(self):
        self.score = 0
        self.score_old = 0
        self.level = 1

    def break_judge(self):
        for i in move.lines:
            judge_filled = 0
            for j in i:
                if j == 1 and move.lines.index(i)<=19:
                    judge_filled += 1
                else:break
            if judge_filled == 10:
                self.break_lines(move.lines.index(i))
                move.lines.remove(i)
                move.lines.insert(0, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def break_lines(self, line):
        self.imgs_re = []
        self.score += int(move.speed*10)
        get_score_sound.play()
        for h in range(len(move.imgs)):
            if move.imgs[h][1][1] == line*30+50:
                self.imgs_re.append(move.imgs[h])
            elif move.imgs[h][1][1] < line*30+50:
                move.imgs[h][1][1] += 30
        for i in self.imgs_re:
            move.imgs.remove(i)