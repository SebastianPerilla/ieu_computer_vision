import numpy as np
import cv2 as cv
from datetime import datetime

# Colors (BGR Format)
SILVER = (192, 192, 192)
DARK_SILVER = (128, 128, 128)
METALLIC_BLUE = (206, 157, 151)
DARK_GRAY = (64, 64, 64)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH, HEIGHT = 512, 512


def main():
    while True:
        img = np.zeros((HEIGHT, WIDTH, 3), np.uint8)
        draw_clock(img)
        cv.imshow('Luxury Watch', img)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()


def draw_clock(img):
    center = (WIDTH // 2, HEIGHT // 2)
    radius = int(WIDTH * 0.3)
    
    # Draw components
    draw_polygon(img, center, radius)
    draw_polygon(img, center, radius - 30, DARK_SILVER, thickness=3)
    draw_hour_markers(img, center, radius - 15)
    draw_bolts(img, center, radius - 15)
    draw_clock_hands(img, center, radius - 30)
    draw_logo(img, center)
    draw_watch_links(img, center, radius, top=True)
    draw_watch_links(img, center, radius, top=False)


def draw_polygon(img, center, radius, color=SILVER, thickness=2):
    points = [
        (
            int(center[0] + radius * np.cos(angle)),
            int(center[1] + radius * np.sin(angle))
        )
        for angle in [(i * (2 * np.pi / 8)) + (np.pi / 8) for i in range(8)]
    ]
    pts = np.array(points, np.int32).reshape((-1, 1, 2))
    cv.polylines(img, [pts], isClosed=True, color=color, thickness=thickness, lineType=cv.LINE_AA)


def draw_bolts(img, center, radius):
    for angle in [(i * (2 * np.pi / 8)) + (np.pi / 8) for i in range(8)]:
        x, y = int(center[0] + radius * np.cos(angle)), int(center[1] + radius * np.sin(angle))
        cv.circle(img, (x, y), 7, SILVER, -1, lineType=cv.LINE_AA)
        cv.line(img, (x - 3, y - 3), (x + 3, y + 3), DARK_GRAY, 2, lineType=cv.LINE_AA)


def draw_logo(img, center):
    text, font, scale, thickness = 'IMC', cv.FONT_HERSHEY_DUPLEX, 0.5, 1
    text_size = cv.getTextSize(text, font, scale, thickness)[0]
    pos = (center[0] - text_size[0] // 2, center[1] - 60)
    cv.putText(img, text, pos, font, scale, SILVER, thickness, cv.LINE_AA)


def draw_hour_markers(img, center, radius):
    for i in range(12):
        angle = (i * (2 * np.pi / 12)) - (np.pi / 2)
        start = (int(center[0] + (radius - 44) * np.cos(angle)), int(center[1] + (radius - 44) * np.sin(angle)))
        end = (int(center[0] + (radius - 23) * np.cos(angle)), int(center[1] + (radius - 23) * np.sin(angle)))
        cv.line(img, start, end, SILVER, 3, cv.LINE_AA)


def draw_clock_hands(img, center, radius):
    now = datetime.now()
    hands = [
        ((now.hour % 12 + now.minute / 60) * (2 * np.pi / 12) - (np.pi / 2), 0.5, 4, SILVER),
        ((now.minute + now.second / 60) * (2 * np.pi / 60) - (np.pi / 2), 0.7, 3, SILVER),
        (now.second * (2 * np.pi / 60) - (np.pi / 2), 0.8, 2, METALLIC_BLUE)
    ]
    
    for angle, length_ratio, thickness, color in hands:
        x, y = int(center[0] + radius * length_ratio * np.cos(angle)), int(center[1] + radius * length_ratio * np.sin(angle))
        cv.line(img, center, (x, y), color, thickness, cv.LINE_AA)
    
    cv.circle(img, center, 8, SILVER, -1, lineType=cv.LINE_AA)
    cv.circle(img, center, 3, DARK_GRAY, -1, lineType=cv.LINE_AA)


def draw_watch_links(img, center, radius, top=True):
    start_angle = (3 if top else 4) * (2 * np.pi / 8) + (np.pi / 8)
    end_y_offset = -radius if top else radius
    
    x1, y1 = int(center[0] + radius * np.cos(start_angle)), int(center[1] + radius * np.sin(start_angle))
    x2, y2 = int(center[0] - radius * np.cos(start_angle)), int(center[1] - radius * np.sin(start_angle))
    end_y = int(center[1] + end_y_offset)
    
    cv.line(img, (x1, y1), (x1 + 60, end_y), SILVER, 2, cv.LINE_AA)
    cv.line(img, (x2, y2), (x2 - 60, end_y), SILVER, 2, cv.LINE_AA)
    cv.line(img, (x1 + 60, end_y), (x2 - 60, end_y), SILVER, 2, cv.LINE_AA)
    
    link_y = end_y + 30 if not top else end_y - 30
    cv.line(img, (x1 + 60, end_y), (x1 + 65, link_y), SILVER, 2, cv.LINE_AA)
    cv.line(img, (x2 - 60, end_y), (x2 - 65, link_y), SILVER, 2, cv.LINE_AA)
    cv.line(img, (x1 + 60, link_y), (x2 - 65, link_y), SILVER, 2, cv.LINE_AA)
    
    left_x, right_x, current_y, link_height = x1 + 65, x2 - 65, link_y, 30
    while 10 < current_y + link_height < HEIGHT - 10 if not top else current_y - link_height > 10:
        cv.line(img, (left_x, current_y), (left_x, current_y + link_height if not top else current_y - link_height), SILVER, 2, cv.LINE_AA)
        cv.line(img, (right_x, current_y), (right_x, current_y + link_height if not top else current_y - link_height), SILVER, 2, cv.LINE_AA)
        cv.line(img, (left_x, current_y + link_height if not top else current_y - link_height), (right_x, current_y + link_height if not top else current_y - link_height), SILVER, 2, cv.LINE_AA)
        current_y += link_height if not top else -link_height

if __name__ == "__main__":
    main()
