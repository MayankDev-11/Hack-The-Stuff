import pyautogui
from PIL import ImageGrab

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):

    for z in range(275, 400):
        for a in range(300, 450):
            continue

    if data[z, a] > 100:
        for l in range(400,445):
            for m in range(200, 330):
                if data[l,m] < 100:
                        hit("down")
                        return True

    if data[z, a] > 100:
        for c in range(400,445):
            for d in range(250, 450):

                if data[l,m] == True:
                    hit("up")

                if data[c,d] < 100:
                    hit("up")
                    return

    if data[z,a] < 100:
        for i in range(400,445):
            for j in range(250, 450):
                if data[i,j] > 100:
                    hit("up")
                    return

    return

if __name__ == "__main__":
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)

        # for i in range(400,445):
        #     for j in range(250, 450):
        #        data[i, j] = 0

        #
        # for i in range(400,445):
        #     for j in range(400, 450):
        #        data[i, j] = 0
        #
        # for i in range(400,445):
        #     for j in range(200, 330):
        #        data[i, j] = 171
        #
        #
        # image.show()
        # break