import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    zodiac = launch_ros.actions.Node(
        package='mypkg',
        executable='zodiac_publisher',
        )
    listener = launch_ros.actions.Node(
            package='mypkg',
            executable='test_listener',
            output='screen'
            )
    
    return launch.LaunchDescription([zodiac, listener]) #([talker, listener])
