""" THis is just a mockup  of code written by me just as a layout and for few key points . It is just a collection of code
 and not an actual game which can run . I have added a lot of classes but many more will be there and note 
that all these classes aren't supposed  to be in a same module .  There will be different modules more data and 
 a lot of more work . This is what  i could code in the time I had . There could be a lot of small silly mistakes do 
 comment on them so i can get rid of them as soon as possible :) """ 



import soy
import sys
import time
import math
import os.path
import random
sys.path.append("data")
import MyGame

 
# Global constants
 
# Colors

 
# Screen dimensions
SCREEN_WIDTH = 
SCREEN_HEIGHT =

 
class Player(object):
    """ PLayer class """
 
    # -- Methods
   def __init__(self, charachter,health) :
        self.charachter = charachter
        self.health = health
        
       
 
        # Call the parent's constructor
        super().__init__()
 
        # Creates a texture for the class
        width = 40
        height = 60
         #New class to be implementd or changes to be figured out
        self.texture = soy.textures.Texture(texture)
        self..material = soy.materials.Textured(colormap=self.texture)

 
        # Set speed vector of player
 
        # List of sprites we can bump against
        self.level = None
 
    def update(self):
        """ Move the player. """
 
        #  hit anything
        def collides(self, scene, other) :
        # soy.atoms.vectors to be used 
        
    def calc_grav(self):
        """ Calculate effect of gravity. """
 
        # on the ground.
 
    def jump(self):
        """ Called when user hits 'jump' button. """
 		
 
    	# Player-controlled movement:
    def go_left(self):
        """ Called when the user hits the left arrow. """
        self.change_x = -6
 
    def go_right(self):
        """ Called when the user hits the right arrow. """
        self.change_x = 6
 
    def stop(self):
        """ Called when the user lets off the keyboard. """
        self.change_x = 0
	def powerupgen(self, position) :
	 # Generates the powerup
        
class Enemy(PLayer) :
    """Base class for all enemies """
    def __init__(self):


    def setup_enemy(self, x, y, direction, name, setup_frames):
        """Sets up various values for enemy"""
        self.sprite_sheet = setup.GFX['smb_enemies_sheet']
        self.frames = []
        self.frame_index = " "
        self.animate_timer = " "
        self.death_timer = " "
        self.gravity = " "
        

        self.name = name
        self.direction = direction
        setup_frames()

       
        self.set_velocity()


    def set_velocity(self):
        """Sets velocity vector based on direction"""

    def get_image(self):
        """Get the image frames from the sprite sheet"""
        

    def handle_state(self):
        """Enemy behavior based on state"""


    def walking(self):
        """Default state of moving sideways"""


    def falling(self):
        """For when it falls off a ledge"""


    def jumped_on(self):
        """Placeholder for when the enemy is stomped on"""
        pass


    def death_jumping(self):
        """Death animation"""


    def start_death_jump(self, direction):
    
    def animation(self):
        """Basic animation, switching between two frames"""
        
    def update(self):
        """Updates enemy behavior"""
     
    def collidePlayer(self, game) :
             .quit 
             
             
    # note :- .soy Importer :- The .soy format is intended to be used within Python with the standard import command. To achieve this PySoy 		adds its importer to sys.path_hooks on initialization. This hook applies to any path added after import soy. 
    # also use .soy Exporter  for  Objects of this class can be populated by PySoy objects and exports them to a file when called. Example usage:

	# export = soy.Exporter()
	# export.mainwindow = soy.widgets.Window('My Game')
	# (...)
	# export('data/MyGame')

 class SonicSpeed() :
    sprite  = " "
    
    def __init__(self) :
       
    def collidePlayer(self, game) :


class Lives(PLayer) :
    sprite = " "
    
    def __init__(self) :
        if HealthUp.model is None :
            HealthUp.model = Model(model)
        
 
        # Display the health and lives 
class bar(soy.widgets.Container) :
    def __init__(self) :
 
class Level(object):
 
    def __init__(self, player):
      
        # Background image
        self.background = None
 
    # Update everythign on this level
    def update(self):
        """ Update everything in this level."""
        self.platform_list.update()
        self.enemy_list.update()
 
    def draw(self, screen):
        """ Draw everything on this level. """
 
        # SPrite in the background
        screen.fill(BLUE)
    # Everything managing sound goes here 
class Sound(object):
    """Handles all sound for the game"""
    def __init__(self, overhead_info):
        """Initialize the class"""
        self.sfx_dict = setup.SFX

    def set_music(self):
        """Sets music for level"""

    def update(self, game_info):
        """Updates sound object with game info"""

    def  handle_state(self):
        """Handles the state of the soundn object"""
   
    def play_music(self, key, state):
        """Plays new music"""
        music.play()
        self.state = state

    def stop_music(self):
        """Stops playback"""
         music.stop()

# Create platforms for the level 1
class Level_01(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
 # Create platforms for the level 1
class Level_02(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
        
        # Create platforms for the level 1
class Level_03(Level):
    """ Definition for level 1. """
 
    def __init__(self, player):
        """ Create level 1. """
 
        # Call the parent constructor
        Level.__init__(self, player)
 
 class Sound(object):
    """Handles all sound for the game"""
    def __init__(self, overhead_info):
        """Initialize the class"""
        
class Checkpoint(soy.textures.Textures):
    """Invisible sprite used to add enemies"""
    def __init__(self, x, name, y=, width=, height=):
        super(Checkpoint, self).__init__()

        
        
        
        
# Just some  Important notes for things that might be needed in future
""" 
#include<pysoy.h>  [Class PROP]
#include<pysoy-utils.h> [_soyGeneratorClass]
module - SImplex2d.c
Action.c
WIndow.C
Material.C
soy.scenes._world  [ a single world for all scenes]
sce.gravity = (0,0,0)
sce.friction = 1
Client. Client [to manage window creation, define context and data state of the object e.t.c. ]
 soy.scenes.Scene.collide_glslf
 _soy.Client_object [ to create client instances locally]
  p = soy.atoms.Position((10, 10, 0))
  a = soy.atoms.Area((10, 10, 20, 0))
  a = soy.atoms.Axis((10, 10, 0)) 
  >>> c = soy.atoms.Color('darksalmon')\n"
>>> c\n"
<Color (233, 150, 122, 255)>\n"
>>> c.red\n"
233\n"
soy.Client Type
PySoy clients manage the state of a specific game instance including
windows, audio input/output, controllers, and object data state.
Instances of this type represent PySoy clients, either local or remote.
Local clients are created by instantating a new soy.Client object and\n"
adding it to a Server. 
Local clients are intended primarily for developing and debugging games
though they may be used for playing downloaded games or local 3D access
 for server administrators.
Due to differing hardware, some properties (position, size, title, etc)
 may be read-only for some clients where these values cannot be changed.
  An exception will be raised when a Client property cannot be changed.
Camera([position, radius]

A camera is an invisible object in 3d space through which the scene can
  be rendered.  It must be attached to a :class:`soy.widgets.Projector`
  or other rendering class to be activated::
>>> room = soy.scenes.Room(3.0)  -  [this line creates a scene called room.]
>>> room['cam'] = soy.bodies.Camera() [This line creates a Camera inside the scene called cam]
>>> client = soy.Client() [This line creates a local Client called client.]
>>> client.window.append(soy.widgets.Projector(room['cam'])) [This line creates a Projector that projects the image from cam on
to the window of the client.
 To project an image with a Projector, you need to append it to a Widget
such as a window to project it on, and a Camera.
A camera can be used by multiple output objects at the same time.
You can move the Camera like any other body.
 For example:
room['cam'].position.z = 15
This moves the Camera's coordinate z to 15
Like other bodies, Camera can also have physics applied to it; such as velocity.
Unlike other bodies, however, Camera do not effect other bodies whenthey collide.
The position of the camera will specify where the scene will be viewed
 from.The X,Y,Z position of the camera  soy.atoms.Position
 py:class:: Portal

"Portal is a portal body.
"Portal has target property for the corresponding portal.
"Example:
scene = soy.scenes.Scene()
portal = soy.bodies.Portal()


py:class:: LandscapeBody([position, size, material]) 
Box shaped body.
 Example::
 >>> b = soy.bodies.LandscapeBody(position=(0.0, 1.0, 8.0), size=(3.0, 2.4, 1.6), material = soy.materials.Colored())
>>> b
 <Box>

py:class:: Projector(camera)

Instances of this class are used to project, as if to a movie screen,
 the output of a soy.bodies.Camera to a 2d area of a Window.
 The camera property can be changed at any time to switch the rendering
perspective to a different position.  Setting the camera property to
None disables rendering.



""""



def main():
    """ Main Program """
    soy.init()
     """Add states to control here."""
 
    # Set the height and width of the screen
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
   display.set_caption("Platformer Jumper")
 
    # Create the player
    player = Player()
 
    # Create all the levels
    level_list = []
    level_list.append( Level_01(player) )
 
    # Set the current level
    current_level_no =
    current_level = level_list[current_level_no]
    """# soy._internals.LoopThread
       # soy.transports.Transport 
       # soy.scenes.scenes"""
    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = soy.time.Clock()
 
    # -------- Main Program Loop ----------- [soy.controllers.Keyboard will be used ] 
  #  while not done:
   #     for event in soy.controllers.Keyboard()
   #     and while loop for the keys assgined
        # Update the player.
        active_sprite_list.update()
 
        # Update items in the level
        current_level.update()
 
        # If the player gets near the right side, shift the world left (-x)
        if
 
        # If the player gets near the left side, shift the world right (+x)
     
 
        # ALL CODE TO DRAW BELOW THIS COMMENT
        current_level.draw(screen)
        active_sprite_list.draw(screen)
 
        # ALL CODE TO DRAW  ABOVE THIS COMMENT
 
        # Limit to 60 frames per second
        clock.tick(60)
 
        #  update the screen .
        display.flip()
 
    
    # on exit.
    .quit()
 
if __name__ == "__main__":
    main()
