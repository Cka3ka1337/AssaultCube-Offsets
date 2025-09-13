from ctypes import (
    Structure, c_float,
    c_int, c_byte
)


WNAME = 'AssaultCube'
PNAME = 'ac_client.exe'

# Structures
VIEW_MATRIX = 0x17DFD0
ENTITY_LIST = 0x18AC04 # entity_list + 0x4 * (i + 1)
LOCAL_PLAYER = 0x17E0A8
COUNT_PLAYERS = 0x18AC0C
GAMEMODE = 0x18ABF8

# To search for the name of the weapon in your hands
# def get_current_gun(ptr: int) -> str
    # struct = mem.read_long(ptr + CURRENT_WEAPON_STRUCT)

    # if not struct:
    #     return ''

    # struct = mem.read_long(struct + CURRENT_WEAPON_NAME)
    # name = mem.read_bytes(struct, 11)
    # return name.strip(b'\x00').decode()
CURRENT_WEAPON_STRUCT = 0x364
CURRENT_WEAPON_NAME = 0xC


# Entity player structure
HeadPos             = 0x4     #    Vec3
Velocity            = 0x10    #    Vec3
MoveOffset          = 0x1c    #    Vec3
Pos                 = 0x28    #    Vec3
Direction           = 0x34    #    Vec2
Recoil              = 0x40    #    c_float
PlayerH             = 0x50    #    c_float
PlayerHM            = 0x54    #    c_float
AutoJump            = 0x5f    #    c_byte_Array_1 - BOOL
Health              = 0xec    #    c_int
Armor               = 0xf0    #    c_int
pistolAmmo          = 0x12c   #    c_int
carbineAmmo         = 0x130   #    c_int
shotgunAmmo         = 0x134   #    c_int
subgunAmmo          = 0x138   #    c_int
sniperAmmo          = 0x13c   #    c_int
assaultAmmo         = 0x140   #    c_int
grenadeAmmo         = 0x144   #    c_int
dualAmmo            = 0x148   #    c_int
knifeAmmo           = 0x14c   #    c_int
pistolDelay         = 0x150   #    c_int
carbineDelay        = 0x154   #    c_int
shotgunDelay        = 0x158   #    c_int
subgunDelay         = 0x15c   #    c_int
sniperDelay         = 0x160   #    c_int
assaultDelay        = 0x164   #    c_int
dualDelay           = 0x168   #    c_int
knifeDelay          = 0x16c   #    c_int
Username            = 0x200   #    c_byte_Array_16
TeamNum             = 0x30c   #    c_int
CurrentWeaponStruct = 0x364   #    c_int_Array_1 # CURRENT_WEAPON_STRUCT
HeadBone            = 0x3f8   #    Vec3


# MAX_AMMO
pistol  = 10
carbine = 10
shotgun = 7
subgun  = 30
sniper  = 5
assault = 20
grenade = 3
dual    = 20
knife   = 0



class ViewMatrix(Structure):
    _fields_ = [
        ('m11', c_float), ('m12', c_float), ('m13', c_float), ('m14', c_float),
        ('m21', c_float), ('m22', c_float), ('m23', c_float), ('m24', c_float),
        ('m31', c_float), ('m32', c_float), ('m33', c_float), ('m34', c_float),
        ('m41', c_float), ('m42', c_float), ('m43', c_float), ('m44', c_float)
    ]
    
    
class Vec2(Structure):
    _fields_ = [
        ('x', c_float), ('y', c_float)
    ]


class Vec3(Structure):
    _fields_ = [
        ('x', c_float), ('y', c_float), ('z', c_float)
    ]


class Entity(Structure):
    _fields_ = [
        ('', c_int),
        ('HeadPos', Vec3),
        ('Velocity', Vec3),
        ('MoveOffset', Vec3),
        ('Pos', Vec3),
        ('Direction', Vec2),
        ('', c_int),
        ('Recoil', c_float),
        ('', c_int * 3),
        ('PlayerH', c_float),
        ('PlayerHM', c_float),
        ('', c_int * 1),
        ('', c_byte * 3),
        ('AutoJump', c_byte * 1),
        ('', c_int * 35),
        ('Health', c_int),
        ('Armor', c_int),
        ('', c_int * 14),
        ('pistolAmmo', c_int),
        ('carbineAmmo', c_int),
        ('shotgunAmmo', c_int),
        ('subgunAmmo', c_int),
        ('sniperAmmo', c_int),
        ('assaultAmmo', c_int),
        ('grenadeAmmo', c_int),
        ('dualAmmo', c_int),
        ('knifeAmmo', c_int),
        ('pistolDelay', c_int),
        ('carbineDelay', c_int),
        ('shotgunDelay', c_int),
        ('subgunDelay', c_int),
        ('sniperDelay', c_int),
        ('assaultDelay', c_int),
        ('dualDelay', c_int),
        ('knifeDelay', c_int),
        ('', c_int * 36),
        ('Username', c_byte * 16),
        ('', c_int * 63),
        ('TeamNum', c_int),
        ('', c_int * 21),
        ('CurrentWeaponStruct', c_int * 1),
        ('', c_int * 36),
        ('HeadBone', Vec3)
    ]