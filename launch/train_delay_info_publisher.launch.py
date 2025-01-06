import launch
import launch.actions
import launch.substitutions
import launch_ros.actions


def generate_launch_description():

    train_info = launch_ros.actions.Node(
        package='mypkg',
        executable='train_info_publisher',
        )
    listener = launch_ros.actions.Node(
            package='mypkg',
            executable='test_listener',
            output='screen'
            )
    
    return launch.LaunchDescription([train_info, listener]) #([talker, listener])
