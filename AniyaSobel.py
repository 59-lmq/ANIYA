import cv2
import numpy as np


def Sobel_demo(image):
    sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0)
    sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1)
    sobel_x = cv2.convertScaleAbs(sobel_x)
    sobel_y = cv2.convertScaleAbs(sobel_y)
    sobel_xy = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 0)
    return sobel_xy


def main():
    cap = cv2.VideoCapture("1.mp4")
    output_path = './output1/aniya_'

    parameter_a = 2/5
    frame_width = int(cap.get(3)*parameter_a*2)
    frame_height = int(cap.get(4)*parameter_a)
    video_out = cv2.VideoWriter('3.mp4',
                                cv2.VideoWriter_fourcc(*'mp4v'),
                                10, (frame_width, frame_height))
    try:
        i = 0
        while True:
            i += 1
            _, img = cap.read()
            if _:
                h, w, c = img.shape
                img = cv2.resize(img, (int(w*parameter_a), int(h*parameter_a)))
                s_img = Sobel_demo(img)
                show_img = np.concatenate([img, s_img], axis=1)  # 横向拼接
                cv2.imwrite(output_path + str(i) + '.jpg', show_img)
                video_out.write(show_img)
                cv2.imshow("ANIYA", show_img)
                cv2.waitKey(int(1/30))
            else:
                cap.release()
                video_out.release()
                cv2.destroyAllWindows()
                break
    except KeyboardInterrupt:
        cap.release()
        video_out.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
