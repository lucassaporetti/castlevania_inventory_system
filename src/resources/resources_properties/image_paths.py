class ImagePaths:
    def __init__(self, image_index):
        self.image_index = image_index

    def get_image(self):
        if self.image_index == 0:
            return '/home/lucassaporetti/GIT-Repository/' \
                   'castlevania_inventory_system/src/' \
                   'resources/images/backgrounds/alucard_weapon_pose.png'

        elif self.image_index == 1:
            return '/home/lucassaporetti/GIT-Repository/' \
                   'castlevania_inventory_system/src/' \
                   'resources/images/backgrounds/richter_weapon_pose.png'

        elif self.image_index == 2:
            return '/home/lucassaporetti/GIT-Repository/' \
                   'castlevania_inventory_system/src/' \
                   'resources/images/backgrounds/alucard_shield_pose.png'

        elif self.image_index == 3:
            return '/home/lucassaporetti/GIT-Repository/' \
                   'castlevania_inventory_system/src/' \
                   'resources/images/backgrounds/dracula_pose.png'

        elif self.image_index == 4:
            return '/home/lucassaporetti/GIT-Repository/' \
                   'castlevania_inventory_system/src/' \
                   'resources/images/backgrounds/alucard_relic_pose.png'

        elif self.image_index == 5:
            return '/home/lucassaporetti/GIT-Repository/' \
                   'castlevania_inventory_system/src/' \
                   'resources/images/backgrounds/dracula_pose2.png'

        elif self.image_index == 6:
            return '/home/lucassaporetti/GIT-Repository/' \
                   'castlevania_inventory_system/src/' \
                   'resources/images/backgrounds/richter_sit_pose.png'

        elif self.image_index == 7:
            return '/home/lucassaporetti/GIT-Repository/' \
                    'castlevania_inventory_system/src/' \
                    'resources/images/backgrounds/system_logo.png'
