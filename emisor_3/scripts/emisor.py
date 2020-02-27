#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32

def talker():
    pub = rospy.Publisher('emisor_1', Float32, queue_size=10)
    rospy.init_node('Ejer_1', anonymous=True) 
    rate = rospy.Rate(10) # 10hz
    
    while not rospy.is_shutdown():
        counter=float(input("introduce un numero:"))
        #counter= str(counter)
        texto='Su numer es: '+ str(counter)
        rospy.loginfo(texto)
        pub.publish(counter)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass 
