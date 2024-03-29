import os
import shutil


def add_init():
    return "        try:\n", "            self.init()\n", "        except AttributeError:\n", "            pass\n"


def anim_class(compil, anim):
    images = anim.properties["Images"]
    timer = str(anim.properties["Timer"])
    flipx = str(anim.properties["Flip X"])
    flipy = str(anim.properties["Flip Y"])
    sprites = []

    if images != [] and images != "":
        for i in images:
            directory = os.path.join(compil.project.project_folder, compil.project.project_name)
            os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
            filename = os.path.basename(i)
            shutil.copyfile(i, os.path.join(directory, "Images", filename))
            sprites.append("Images/" + filename)

    text = [
        "from pyengine.Components import AnimComponent\n\n\n",
        "class " + anim.name + "(AnimComponent):\n",
        "    def __init__(self):\n",
        "        super(" + anim.name + ", self).__init__(" + timer + ", " + str(sprites) + ", " + flipx + ", " + flipy
        + ")\n"
    ]
    text += add_init()
    if anim.script != "":
        text.append("    \n")
        for i in anim.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def life_class(compil, life):
    mlife = str(life.properties["Vie Max"])
    callback = str(life.properties["Callback"])

    text = [
        "from pyengine.Components import LifeComponent\n\n\n",
        "class " + life.name + "(LifeComponent):\n",
        "    def __init__(self):\n",
        "        super(" + life.name + ", self).__init__(" + mlife + ")\n"
    ]
    text += add_init()
    if callback != "":
        text.append("        self.callback = self." + callback + "\n")
    if life.script != "":
        text.append("    \n")
        for i in life.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def control_class(compil, con):
    type_ = str(con.properties["Type de Controle"])
    speed = str(con.properties["Vitesse"])
    ch = str(con.properties["Controle Haut"])
    cg = str(con.properties["Controle Gauche"])
    cd = str(con.properties["Controle Droit"])
    cb = str(con.properties["Controle Bas"])

    text = [
        "from pyengine.Components import ControlComponent\nfrom pyengine import ControlType, Controls, const\n\n\n",
        "class " + con.name + "(ControlComponent):\n",
        "    def __init__(self):\n",
        "        super(" + con.name + ", self).__init__(ControlType." + type_ + ", " + speed + ")\n"
    ]
    text += add_init()
    text += [
        "        self.set_control(Controls.UPJUMP, const.K_" + ch + ")\n",
        "        self.set_control(Controls.LEFT, const.K_" + cg + ")\n",
        "        self.set_control(Controls.RIGHT, const.K_" + cd + ")\n",
        "        self.set_control(Controls.DOWN, const.K_" + cb + ")\n"
    ]
    if con.script != "":
        text.append("    \n")
        for i in con.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def position_class(compil, pos):
    pos_x = str(pos.properties["Position X"])
    pos_y = str(pos.properties["Position Y"])
    off_x = str(pos.properties["Offset X"])
    off_y = str(pos.properties["Offset Y"])

    text = [
        "from pyengine.Components import PositionComponent\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + pos.name + "(PositionComponent):\n",
        "    def __init__(self):\n",
        "        super(" + pos.name + ", self).__init__(Vec2(" + pos_x + ", " + pos_y + "), Vec2(" + off_x +
        ", " + off_y + "))\n"
    ]
    text += add_init()
    if pos.script != "":
        text.append("    \n")
        for i in pos.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def sprite_class(compil, sprite):
    image = str(sprite.properties["Image"])
    scale = str(sprite.properties["Scale"])
    rot = str(sprite.properties["Rotation"])
    flipx = str(sprite.properties["Flip X"])
    flipy = str(sprite.properties["Flip Y"])

    if image != "":
        directory = os.path.join(compil.project.project_folder, compil.project.project_name)
        os.makedirs(os.path.join(directory, "Images"), exist_ok=True)
        filename = os.path.basename(image)
        shutil.copyfile(image, os.path.join(directory, "Images", filename))
        image = "Images/" + filename

    text = [
        "from pyengine.Components import SpriteComponent\n\n\n",
        "class " + sprite.name + "(SpriteComponent):\n",
        "    def __init__(self):\n",
        "        super(" + sprite.name + ', self).__init__("' + image + '", ' + scale + ", " + rot + ", " + flipx +
        ", " + flipy + ")\n"
    ]
    text += add_init()
    if sprite.script != "":
        text.append("    \n")
        for i in sprite.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def physics_class(compil, phys):
    agravity = str(phys.properties["Affecté par Gravité"])
    fric = str(phys.properties["Friction"])
    elas = str(phys.properties["Elasticité"])
    mass = str(phys.properties["Masse"])
    solid = str(phys.properties["Solide"])
    rotation = str(phys.properties["Rotation"])
    callback = str(phys.properties["Callback"])

    text = [
        "from pyengine.Components import PhysicsComponent\n\n\n",
        "class " + phys.name + "(PhysicsComponent):\n",
        "    def __init__(self):\n",
        "        super(" + phys.name + ", self).__init__(" + agravity + ", " + fric + ", " + elas + ", " + mass + ", "
        + solid + ", " + rotation + ")\n"
    ]
    text += add_init()
    if callback != "":
        text.append("        self.callback = self." + callback + "\n")
    if phys.script != "":
        text.append("    \n")
        for i in phys.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def move_class(compil, move):
    dirx = str(move.properties["Direction X"])
    diry = str(move.properties["Direction Y"])

    text = [
        "from pyengine.Components import MoveComponent\nfrom pyengine.Utils import Vec2\n\n\n",
        "class " + move.name + "(MoveComponent):\n",
        "    def __init__(self):\n",
        "        super(" + move.name + ", self).__init__(Vec2(" + dirx + ", " + diry + "))\n"
    ]
    text += add_init()
    if move.script != "":
        text.append("    \n")
        for i in move.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)


def text_class(compil, txt):
    texte = str(txt.properties["Texte"])
    scale = str(txt.properties["Scale"])
    color = txt.properties["Couleur"]
    font = txt.properties["Font"]
    npolice = str(txt.properties["Nom Police"])
    tpolice = str(txt.properties["Taille Police"])
    ipolice = str(txt.properties["Italique"])
    gpolice = str(txt.properties["Gras"])
    spolice = str(txt.properties["Souligné"])

    text = [
        "from pyengine.Components import TextComponent\nfrom pyengine.Utils import Color, Font\n\n\n",
        "class " + txt.name + "(TextComponent):\n",
        "    def __init__(self):\n",
        "        super(" + txt.name + ', self).__init__("' + texte + '", Color(' + str(color[0]) + ", " +
        str(color[1]) + ", " + str(color[2]) + '), Font("' + npolice + '", ' + tpolice + ", " + ipolice + ", " +
        gpolice + ", " + spolice + ")"
    ]
    if font is not None:
        text.append(", Color(" + str(font[0]) + ", " + str(font[1]) + ", " + str(font[2]) + ")")
    text.append(", scale=" + scale + ")\n")
    text += add_init()
    if txt.script != "":
        text.append("    \n")
        for i in txt.script.split("\n"):
            text.append("    " + i + "\n")
    return "".join(text)