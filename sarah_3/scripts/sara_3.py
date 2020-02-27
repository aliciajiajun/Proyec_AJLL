#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import Float32
# Int16 para entereos ,String cadenas, Float32 para float
def callback(msg):
    rospy.loginfo("mensaje recibido: %s",msg.data)
def memory_subscriber():
    rospy.init_node('suscriptor_sarah',anonymous=True)
    #el primer argumento, es el nombrel del topic al que queremos suscribirnos...
    #el segundo argumento es el tipo de mensaje,
    rospy.Subscriber('emisor_1',Float32,callback)
    rospy.spin()
if __name__ == "__main__":
    try:
        memory_subscriber()
    except rospy.ROSInterruptException:
        pass 