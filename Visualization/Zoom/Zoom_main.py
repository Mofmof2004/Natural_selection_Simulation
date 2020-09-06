from Visualization.Visual_accessories import button
from Visualization.Zoom.Zoom_0 import zoom_0, zoom_1

def add(view_zoom_count):

    return view_zoom_count + 1


view_zoom_count = 0



def zoom_main(agent_list):

    if view_zoom_count == 0:
        print(view_zoom_count)
        zoom_0(agent_list, view_zoom_count)

    elif view_zoom_count > 0:
        print(view_zoom_count)
        zoom_1(agent_list, view_zoom_count)

