

class Helper:
    @staticmethod
    def draw_centered(surface, obj):
        center_x, center_y = surface.get_width() / 2, surface.get_height() / 2
        obj_half_width, obj_half_height = obj.get_width() / 2, obj.get_height() / 2
        surface.blit(obj, (center_x - obj_half_width, center_y - obj_half_height))