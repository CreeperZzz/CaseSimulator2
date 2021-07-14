# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# import pygame.key

import case
import tools
import sqlConnect


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # pygame.init()

    sql = sqlConnect.Sql()

    cid = 0

    # print(sql.get_weaplist(cid))
    # print(sql.get_rate(cid))

    while 1:
        print("Press ENTER to start, Enter q to quit.")
        k = input()
        if k.lower() == 'q': #pk.key.get_pressed()[pygame.K_q]:
            break
        elif k.lower() == '': #pk.key.get_pressed()[pygame.K_r]:
            # res = [tools.randItem() for i in range(1000)]
            # print(res.count('a'), res.count('b'), res.count('c'))
            quality = tools.rand_qua(sql.get_rate(cid))
            weap = tools.rand_weap(sql.get_weaplist_qua(quality, cid))
            # weaplist = sql.get_weaplist_qua(quality, cid)
            print(weap)
        else:
            print("enter again")

    sql.close()

#     import pygame
#     import sys
#
#     pygame.init()  # 初始化pygame
#     size = width, height = 640, 480  # 设置窗口大小
#     screen = pygame.display.set_mode(size)  # 显示窗口
#     color = (0, 0, 0)  # 设置颜色
# #    ball = pygame.image.load('ball.png')  # 加载图片
#     ball = pygame.transform.scale(pygame.image.load('ball.png'), (50, 50))
#     ballrect = ball.get_rect()  # 获取矩形区域
#     speed = [5, 5]  # 设置移动的X轴、Y轴
#     clock = pygame.time.Clock();
#
#     while True:  # 死循环确保窗口一直显示
#         # clock.tick(0)
#         for event in pygame.event.get():  # 遍历所有事件
#             if event.type == pygame.QUIT:  # 如果单击关闭窗口，则退出
#                 pygame.quit()
#                 sys.exit()
#
#         ballrect = ballrect.move(speed)  # 移动小球
#         # 碰到左右边缘
#         if ballrect.left < 0 or ballrect.right > width:
#             speed[0] = -speed[0]
#         # 碰到上下边缘
#         if ballrect.top < 0 or ballrect.bottom > height:
#             speed[1] = -speed[1]
#
#         screen.fill(color)  # 填充颜色(设置为0，执不执行这行代码都一样)
#         screen.blit(ball, ballrect)  # 将图片画到窗口上
#         pygame.display.flip()  # 更新全部显示
#
#     pygame.quit()  # 退出pygame

