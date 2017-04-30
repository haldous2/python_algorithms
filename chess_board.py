class chessBoard:
    """
    A general BFS to find number of jumps via path from start to target
    """

    mem_point = {}
    mem_collide = {}
    mem_outofrange = {}     # memoized: points out of range
    mem_visited = {}        # places we've already moved to

    def get_moves(self, point=(-1,-1), pawns=[]):
        """
        return all moves a piece can make
        """
        points = {}
        x = point[0]
        y = point[1]

        if (x, y) in self.mem_point:
            #print "hit mem_point @ {}".format((x, y))
            for i in xrange(0, 8):
                points[i] = self.mem_point[(x, y)][i] # Points (x,y),(x,y) etc..
            return points

        points[0] = (x+2, y+1)
        points[1] = (x+2, y-1)
        points[2] = (x-2, y+1)
        points[3] = (x-2, y-1)
        points[4] = (x+1, y+2)
        points[5] = (x-1, y+2)
        points[6] = (x+1, y-2)
        points[7] = (x-1, y-2)

        # memoize
        self.mem_point[(x, y)] = [points[i] for i in points]

        return points

    def move_collision(self, start, end, pawns=[]):
        """
        Check if path plows through pawns somehow
        return True or False

        Note: no need to check end move (the hook)
              since returned from get_move will be the end move
              and that is checked in the main function
        """
        x_1 = start[0]
        y_1 = start[1]
        x_2 = end[0]
        y_2 = end[1]

        if (x_1, y_1, x_2, y_2) in self.mem_collide:
            #print "hit mem_collide @ points {}, {}".format((x_1, y_1), (x_2, y_2))
            return self.mem_collide[(x_1, y_1, x_2, y_2)] # True or False

        ret = None # track True or False to end for memoization
        if abs(x_2 - x_1) > abs(y_2 - y_1):
            # x is larger - move x first
            # (1,1) -> (3,2)
            # (3,2) -> (1,1)
            if x_1 > x_2:
                if (x_1 - 1, y_1) in pawns:
                    ret = True
                if (x_1 - 2, y_1) in pawns:
                    ret = True
            else:
                if (x_1 + 1, y_1) in pawns:
                    ret = True
                if (x_1 + 2, y_1) in pawns:
                    ret = True
        else:
            # y is larger - move y first
            if y_1 > y_2:
                if (x_1, y_1 - 1) in pawns:
                    ret = True
                if (x_1, y_1 - 2) in pawns:
                    ret = True
            else:
                if (x_1, y_1 + 1) in pawns:
                    ret = True
                if (x_1, y_1 + 2) in pawns:
                    ret = True

        if ret:
            self.mem_collide[(x_1, y_1, x_2, y_2)] = True
            return True
        self.mem_collide[(x_1, y_1, x_2, y_2)] = False
        return False

    def move_out_of_range(self, start, target, point):
        """
        Checking to see if point is getting too far out of range
        range will be a distance multipled from start to target (arbitrary)
        ** note: there might be an actual way to calculate the best out of range.. for now, this is it

        start = original start
        target = original target
        point = point being tested - the 'move'
        """

        distance_multiplier = 2

        # calculate four corners of 'box'

        # x, y of points
        x_1 = start[0]
        y_1 = start[1]
        x_2 = target[0]
        y_2 = target[1]
        x_p = point[0]
        y_p = point[1]

        if (x_p, y_p) in self.mem_outofrange:
            #print "hit mem_collide @ points {}, {}".format((x_1, y_1), (x_2, y_2))
            return self.mem_outofrange[(x_p, y_p)] # True or False

        # distance x, y .. start to target
        # calculating 1/4th extra padding for all sides
        d_x = abs(x_1 - x_2) * distance_multiplier // 4
        d_y = abs(y_2 - y_2) * distance_multiplier // 4

        if x_1 > x_2:
            x_l = x_2 - d_x
            x_r = x_1 + d_x
        else:
            x_l = x_1 - d_x
            x_r = x_2 + d_x

        if y_1 > y_2:
            y_t = y_1 + d_y
            y_b = y_2 - d_y
        else:
            y_t = y_2 + d_y
            y_b = y_1 - d_y

        ret = None

        if x_p < x_l or x_p > x_r:
            ret = True
        if y_p < y_b or y_p > y_t:
            ret = True

        # if ret:
        #     print "point:({},{}) target:({},{}) NOT in bounds of ({},{}),({},{}),({},{}),({},{})".format(x_p, y_p, x_2, y_2, x_l, y_t, x_r, y_t, x_l, y_b, x_r, y_b)
        # else:
        #     print "point:({},{}) target:({},{}) in bounds of ({},{}),({},{}),({},{}),({},{})".format(x_p, y_p, x_2, y_2, x_l, y_t, x_r, y_t, x_l, y_b, x_r, y_b)

        if ret:
            self.mem_outofrange[(x_p, y_p)] = True
            return True
        self.mem_outofrange[(x_p, y_p)] = False
        return False

    def chess_board(self, start, target, pawns=[]):
        """
        basic bfs for a grid'like' structure
        find path from start to target, this class does not allow to jump over pawns
        start = point(x,y)
        target = point(x,y) - goal
        pawns = list of points(x,y)
        """

        q = [[start]]
        path = []
        paths = []

        while q:

            path = q.pop(0)
            point = path[-1]
            #print q

            if point == target:
                paths.append(path)
                # only need to find one path, break out.. otherwise keep looking
                break

            # get moves
            # returning dict {0:(1,2),1:(2,2),etc..}
            moves = self.get_moves((point[0], point[1]))

            for move in [moves[i] for i in moves]:

                """
                skip adding to path when:
                 move has already been visited
                 move is a pawn
                 point to move travels over a pawn spot
                """
                #if (move in self.mem_visited or
                #    move in pawns or
                #    self.move_collision(point, move, pawns) or
                #    self.move_out_of_range(start, target, move)):
                if (move in self.mem_visited or
                    move in pawns):
                    continue

                self.mem_visited[move] = True

                new_path = list(path)
                new_path.append(move)
                q.append(new_path)

        if paths:
            print "paths:", paths, "length:", len(paths[0])
            print "points:{} collisions:{} outofrange:{} visited:{}".format(len(self.mem_point), len(self.mem_collide), len(self.mem_outofrange), len(self.mem_visited))
        else:
            print "no paths found"

chess_board = chessBoard()
#chess_board.chess_board((5,5), (10,10), [])
#chess_board.chess_board((5,5), (12,22), [])
chess_board.chess_board((5,5), (12,19), [(10,11),(10,9),(9,10),(10,12),(10,13),(10,8),(10,7)])
