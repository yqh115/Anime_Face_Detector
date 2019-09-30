import os
import json

rootFolder = os.listdir("C:/Users/ME/Desktop/new/")
f1 = open('C:/Users/ME/Desktop/text_data.txt', 'w')
for name in rootFolder:
    print(name)
    with open(os.path.join("C:/Users/ME/Desktop/new/", name)) as f:
        load_dict = json.load(f)
    f.close()
    if (load_dict['flags']['half_face'] == True):
        result = name[:-5] + " 1 " + "0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        f1.write(result + "\n")
        continue
    if (load_dict['flags']['no_face'] == True):
        result = name[:-5] + " 0 " + "0 0 0 0 0 0 0 0 0 0 0 0 0 0"
        f1.write(result + "\n")
        continue
    if (load_dict['flags']['face'] == True):
        for instance in load_dict['shapes']:
            if (instance['label'] == 'lefteye'):
                lefteye_points = instance['points'][0]
            if (instance['label'] == 'righteye'):
                righteye_points = instance['points'][0]
            if (instance['label'] == 'nose'):
                nose_points = instance['points'][0]
            if (instance['label'] == 'leftmouth'):
                leftmouse_points = instance['points'][0]
            if (instance['label'] == 'rightmouth'):
                rightmouse_points = instance['points'][0]
            if (instance['label'] == 'left_top'):
                leftbottom_points = instance['points'][0]
            if (instance['label'] == 'right_bottom'):
                rightup_points = instance['points'][0]

        result = name[:-5] + " " + "1 " + str(leftbottom_points[0]) + " " + str(rightup_points[0]) + " " + str(
            rightup_points[1]) + " " + str(leftbottom_points[1]) + " " + str(lefteye_points[0]) + " " + str(
            lefteye_points[1]) + " " + str(righteye_points[0]) + " " + str(righteye_points[1]) + " " + str(
            nose_points[0]) + " " + str(nose_points[1]) + " " + str(leftmouse_points[0]) + " " + str(
            leftmouse_points[1]) + " " + str(rightmouse_points[0]) + " " + str(rightmouse_points[1])
        f1.write(result + "\n")
f1.close()
