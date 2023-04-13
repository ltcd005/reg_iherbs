import random


def typing(page,element,value):
        for v in value:
            element.press(v)
            page.wait_for_timeout(int(random.uniform(0.1,0.5))*1000)

def touch(page,element):
    element_bounding_box  = element.bounding_box()
    x_range = random.uniform(element_bounding_box["x"],element_bounding_box["x"] + element_bounding_box["width"])
    y_range = random.uniform(element_bounding_box["y"],element_bounding_box["y"] + element_bounding_box["height"])
    page.mouse.click(x_range,y_range)

def wait_for_url_helper(page,target_url,timeout):
    for _ in range(timeout):
        current_url = page.url
        if target_url in current_url:
            return True
        else:
            page.wait_for_timeout(1000)
    return False
