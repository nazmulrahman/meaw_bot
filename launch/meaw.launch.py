from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Custom controller node
        Node(
            package='meaw_bot',
            executable='controller',
            name='controller_node',
            output='screen'
        ),

        # Camera node
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

        # WebSocket server for web app
        Node(
            package='rosbridge_server',
            executable='rosbridge_websocket',
            name='rosbridge_websocket',
            output='screen'
        ),

        # MJPEG video stream server
        Node(
            package='web_video_server',
            executable='web_video_server',
            name='web_video_server',
            output='screen'
        )
    ])
