class King(Piece):
    def possible_moves(self):
        L=[]
        try :
            L+=[self.position._get_diagonal_upleft()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_diagonal_upright()]
        except AssertionError  :
            pass
        try:
            L+=[self.position._get_diagonal_downleft()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_diagonal_downright()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_down()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_up()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_right()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_left()]
        except AssertionError :
            pass
        for p in L:
            if p._get_piece()!=None:
                L.remove(p)
        return [i.position for i in L]
    def possible_attacks(self):
        L=[]
        try :
            L+=[self.position._get_diagonal_upleft()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_diagonal_upright()]
        except AssertionError  :
            pass
        try:
            L+=[self.position._get_diagonal_downleft()]
        except AssertionError :
            pass
        try:
            L+=[self.position._get_diagonal_downright()]
        except AssertionError :
            pass
        try:
            L+=[self._get_up(),self._get_down()]
        except AssertionError :
            pass
        try:
            L+=[self._get_right()]
        except AssertionError :
            pass
        try:
            L+=[self._get_left()]
        except AssertionError :
            pass
        for p in L:
            if p._get_piece()==None or p._get_piece().team==self.team:
                L.remove(p)
        return [i.position for i in L]
