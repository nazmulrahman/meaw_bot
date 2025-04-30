from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Your custom controller.py node
        Node(
            package='meaw_bot',
            executable='controller',
            name='controller_node',
            output='screen'
        ),

        # Webcam publisher node
        Node(
            package='v4l2_camera',
            executable='v4l2_camera_node',
            name='usb_cam',
            parameters=[{
                'image_size': [640, 480],
                'camera_frame_id': 'camera_frame'
            }],
            output='screen'
        ),
    ])
