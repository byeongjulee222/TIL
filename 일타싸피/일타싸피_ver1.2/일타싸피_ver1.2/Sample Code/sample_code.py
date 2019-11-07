import socket
import time
import math

# User and Game Server Information
NICKNAME = 'Byeongju Lee'
HOST = '127.0.0.1'
PORT = 1447 # Do not modify

# predefined variables(Do not modify these values)
TABLE_WIDTH = 254
TABLE_HEIGHT = 124
NUMBER_OF_BALLS = 5
HOLES = [ [0, 0], [130, 0], [260, 0], [0, 130], [130, 130], [260, 130] ]

class Conn:
    def __init__(self):
        self.sock = socket.socket()
        print('Trying to Connect: ' + HOST + ':' + str(PORT))
        self.sock.connect((HOST, PORT))
        print('Connected: ' + HOST + ':' + str(PORT))
        send_data = '9901/' + NICKNAME
        self.sock.send(send_data.encode('utf-8'))
        print('Ready to play.\n--------------------')
    def request(self):
        self.sock.send('9902/9902'.encode())
        print('Received Data has been currupted, Resend Requested.')
    def receive(self):
        recv_data = (self.sock.recv(1024)).decode()
        print('Data Received: ' + recv_data)
        return recv_data
    def send(self, angle, power):
        merged_data = '%d/%d' % (angle, power)
        self.sock.send(merged_data.encode('utf-8'))
        print('Data Sent: ' + merged_data)
    def close(self):
        self.sock.close()

class GameData:
    def __init__(self):
        self.reset()
    def reset(self):
        self.balls = [[0, 0] for i in range(NUMBER_OF_BALLS)]
    def read(self, conn):
        recv_data = conn.receive()
        split_data = recv_data.split('/')
        idx = 0    
        try:
            for i in range(NUMBER_OF_BALLS):
                for j in range(2):
                    self.balls[i][j] = int(split_data[idx])
                    idx += 1
        except:
            self.reset()
            conn.request()
            self.read(conn)
    def show(self):
        print('=== Arrays ===')
        for i in range(NUMBER_OF_BALLS):
            print('Ball%d: %d, %d' % (i, self.balls[i][0], self.balls[i][1]))
        print()

# 자신의 차례가 되어 게임을 진행해야 할 때 호출되는 Method
def play(conn, gameData):
    angle = 10
    power = 10

    # print(gameData.balls)
    # if gameData.balls[1] == [125, 120]:
    #     angle = 50
    #     power = 50
    
    # elif gameData.balls[1] == [250, 10]:
    #     angle = 105
    #     power = 100

    # elif gameData.balls[2] == [15, 10]:
    #     angle = 267
    #     power = 100
    
    # elif gameData.balls[2] == [240, 124]:
    #     angle = 86.5
    #     power = 75
    
    # elif gameData.balls[3] == [250, 10]:
    #     angle = 182.7
    #     power = 70
    
    # elif gameData.balls[3] == [254, 6]:
    #     angle = 90
    #     power = 30

    # elif gameData.balls[1] == [195, 65]:
    #     angle = 89
    #     power = 180

    # elif gameData.balls[1] == [254, 58]:
    #     angle = 180
    #     power = 80
    
    ######################################################################################
    # 주어진 정보를 바탕으로 샷을 할 방향과 세기를 결정해서 angle, power 값으로 지정 #
    ######################################################################################
    balls = gameData.balls
    
    # print(start[0], start[1])

    # 반복 횟수 설정 위해
    # empty = balls.count([0, 0])
    # print(empty)


    start = gameData.balls[0]

    if balls[1] != [0, 0]:
    # 가까운 구멍 찾기
        Min = 9999
        for hole in HOLES:
            if ((hole[0]-start[0])**2+(hole[1]-start[1])**2)**0.5 < Min:
                Min = ((hole[0]-start[0])**2+(hole[1]-start[1])**2)**0.5
                Goal = [hole[0], hole[1]]

        ball_to_goal_angle = math.atan((Goal[1] - balls[1][1])/(Goal[0] - balls[1][0]))
        print(ball_to_goal_angle*math.pi/180)
        shot_point_x, shot_point_y = balls[1][0] + 7.5*math.cos(ball_to_goal_angle*math.pi/180), balls[1][1] + 7.5*math.sin(ball_to_goal_angle*math.pi/180)

        angle = 90 - math.atan((shot_point_y - start[1])/(shot_point_x - start[0]))*(180/math.pi)
        power = (((balls[1][1]-start[1])**2+(balls[1][0]-start[0])**2)**0.5) * 0.6

        conn.send(angle, power)
        
    elif balls[2] != [0, 0]:
    # 가까운 구멍 찾기
        Min = 9999
        for hole in HOLES:
            if ((hole[0]-start[0])**2+(hole[1]-start[1])**2)**0.5 < Min:
                Min = ((hole[0]-start[0])**2+(hole[1]-start[1])**2)**0.5
                Goal = [hole[0], hole[1]]

        ball_to_goal_angle = math.atan((Goal[1] - balls[2][1])/(Goal[0] - balls[2][0]))
        print(ball_to_goal_angle*math.pi/180)
        shot_point_x, shot_point_y = balls[2][0] + 7.5*math.cos(ball_to_goal_angle*math.pi/180), balls[2][1] + 7.5*math.sin(ball_to_goal_angle*math.pi/180)

        angle = 90 - math.atan((shot_point_y - start[1])/(shot_point_x - start[0]))*(180/math.pi)
        power = (((balls[2][1]-start[1])**2+(balls[2][0]-start[0])**2)**0.5) * 0.6

        conn.send(angle, power)
  
    elif balls[3] != [0, 0]:
    # 가까운 구멍 찾기
        Min = 9999
        for hole in HOLES:
            if ((hole[0]-start[0])**2+(hole[1]-start[1])**2)**0.5 < Min:
                Min = ((hole[0]-start[0])**2+(hole[1]-start[1])**2)**0.5
                Goal = [hole[0], hole[1]]

        ball_to_goal_angle = math.atan((Goal[1] - balls[3][1])/(Goal[0] - balls[3][0]))

        shot_point_x, shot_point_y = balls[3][0] + 7.5*math.cos(ball_to_goal_angle*math.pi/180), balls[3][1] + 7.5*math.sin(ball_to_goal_angle*math.pi/180)

        angle = 90 - math.atan((shot_point_y - start[1])/(shot_point_x - start[0]))*(180/math.pi)
        power = (((balls[3][1]-start[1])**2+(balls[3][0]-start[0])**2)**0.5) * 0.6

        conn.send(angle, power)

    elif balls[4] != [0, 0]:
    # 가까운 구멍 찾기
        Min = 9999
        for hole in HOLES:
            if ((hole[0]-start[0])**2+(hole[1]-start[1])**2)**0.5 < Min:
                Min = ((hole[0]-start[0])**2+(hole[1]-start[1])**2)**0.5
                Goal = [hole[0], hole[1]]

        ball_to_goal_angle = math.atan((Goal[1] - balls[4][1])/(Goal[0] - balls[4][0]))

        shot_point_x, shot_point_y = balls[4][0] + 7.5*math.cos(ball_to_goal_angle*math.pi/180), balls[4][1] + 7.5*math.sin(ball_to_goal_angle*math.pi/180)

        angle = 90 - math.atan((shot_point_y - start[1])/(shot_point_x - start[0]))*(180/math.pi)
        power = (((balls[4][1]-start[1])**2+(balls[4][0]-start[0])**2)**0.5) * 0.6

        conn.send(angle, power)

    conn.send(angle, power)
                

def main():
    conn = Conn()
    gameData = GameData()
    while True:
        gameData.read(conn)
        gameData.show()
        if gameData.balls[0][0] == 9909:
            break
        play(conn, gameData)        
    conn.close()
    print('Connection Closed')

if __name__ == '__main__':
    main()
