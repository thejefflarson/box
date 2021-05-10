import cadquery as cq
shell_radius = 3
width = 110
height = 110
depth = 50
box = (
    cq
    .Workplane("XY")
    .box(width, height, depth)
    .translate((0, 0, depth / 2 + shell_radius))
    .faces("+Z")
    .shell(2)
    .faces(">Z")
    .workplane()
    .rect(width - shell_radius, height - shell_radius, forConstruction=True)
    .vertices()
    .circle(3)
    .extrude(-1 * depth, combine=True, clean=True)
    .faces(">Z")
    .workplane()
    .rect(width - shell_radius, height - shell_radius, forConstruction=True)
    .vertices()
    .hole(2, 10)
    .faces(">Y")
    .workplane()
    .rarray(35, 50, 3, 2) # dunno why this works, or what's wrong here the y repeat should really only be 1 and 50 is arbitrary
    .hole(28, shell_radius)
)

handle_outer = (
    box
    .faces("<Y")
    .workplane()
    .split(keepTop=True)
    .center(0, -1 * depth / 2)
    .rect(width - 20, depth - 20)
    .workplane(offset=40)
    .rect(width - 30, depth - 30)
    .loft(combine=True)
)

handle_hole = (
    box
    .faces("<Y")
    .workplane()
    .split(keepTop=True)
    .center(0, -1 * depth / 2)
    .rect(width - 25, depth - 19)
    .workplane(offset=36)
    .rect(width - 35, depth - 29)
    .loft(combine=True)
)

handle = handle_outer.cut(handle_hole)

lid = (
    cq
    .Workplane("XY")
    .tag("lid")
    .box(width + shell_radius, height + shell_radius, 4)
    .translate((0, 0, 3))
    .faces("-Z")
    .edges()
    .fillet(shell_radius)
    .faces("-Z")
    .workplane()
    .rect(width - shell_radius, height - shell_radius, forConstruction=True)
    .vertices()
    .cboreHole(2, 4.5, 1.5, depth=None)
    .faces(">Z")
    .workplane()
    .rarray(20, 20, 3, 3)
    .hole(10.1, 4 + shell_radius)
)

show_object(lid)
#show_object((box+handle).translate((width + 5, 0, 0)))

