#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
from geometry_msgs.msg import Point
import math

class infos():

    def __init__(self):
        
        rospy.init_node('p2', anonymous=True)
        rospy.Subscriber('velocidade', Twist, self.calcular)
        self.mod = rospy.Publisher('modulodeV', Point, queue_size=10)

    def calcular(self, V):

        x, y, z = V.linear.x, V.linear.y, V.linear.z
        quadrado = x**2 + y**2 + z**2
        modulo = Point()
        modulo.x = math.sqrt(quadrado)
       

        #não lembro ao certo como se calcula o modulo da velocidade angular
        x2, y2, z2 = V.angular.x, V.angular.y, V.angular.z     
        quadrado2 = x2**2 + y2**2 + z2**2
        modulo.y = math.sqrt(quadrado2)
        
        self.mod.publish(modulo)
        #rospy.loginfo(modulo) #use se quiser conferir se o programa esta rodando certo


if __name__ == '__main__':
    i = infos()
    rospy.spin()