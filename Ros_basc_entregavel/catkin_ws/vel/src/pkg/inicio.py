#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
import random

class run:

    def __init__(self):
        rospy.init_node('p1', anonymous=True)

        self.pub= rospy.Publisher('velocidade', Twist, queue_size=10)


    def inicar(self):

        rate = rospy.Rate(10)
        #gerar numeros da Vel.linear
        V = Twist()

        V.linear.x = random.randint(0,10)
        V.linear.y = random.randint(0,10)
        V.linear.z = random.randint(0,10)

        #gerar numeros da Vel.Angular
        V.angular.x = random.randint(0,10)
        V.angular.y = random.randint(0,10)
        V.angular.z= random.randint(0,10)

        while not rospy.is_shutdown():
            self.pub.publish(V)
            rospy.Subscriber('modulodeV', Point, self.teste)
            rate.sleep()

    def teste(self,k):
        modulo_linear = f'modulo da velocidade linear: {k.x}'
        modulo_angular = f'modulo da velocidade angular: {k.y}'
        rospy.loginfo(modulo_linear)
        rospy.loginfo(modulo_angular)
        

if __name__ == '__main__':
    t = run()
    t.inicar()
    rospy.spin()