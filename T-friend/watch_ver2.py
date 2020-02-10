import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess



TRAIN = False
TEST = False

if not os.path.exists('log_test.txt'):
    with open('log_test.txt', 'w', encoding='utf-8') as w_file:
        w_file.write('log_start\n')
        w_file.close()

# 요청 데이터와 결과데이터 비교하여 리스트 형성
def comp():
    # 요청 디렉토리
    REQ_DiR = '/T-friend_data/test_REQ/dev'
    # 결과 디렉토리
    comp_DIR = '/T-friend_data/test_RES/dev'

    file_name = []
    comp_name = []
    f_list = []

    file_list = os.listdir(REQ_DiR)
    comp_list = os.listdir(comp_DIR)

    for file in file_list:
        name = os.path.splitext(file)
        file_name.append(name[0])

    for comp_file in comp_list:
        c_name = os.path.splitext(comp_file)
        comp_name.append(c_name[0])

    s = set(comp_name)
    temp = [x for x in file_name if x not in s]

    for name in temp:
        f_name = str(name) + '.REQ'
        f_list.append(f_name)

    return f_list


class Target:
    # 요청파일감지 디렉토리
    watchDir = '/T-friend_data/test_REQ/dev'
    # 학습파일감지 디렉토리
    trainDir = '/T-friend_data/test_TRAIN/dev'
    #watchDir에 감시하려는 디렉토리를 명시한다.


    def __init__(self):
        self.observer = Observer()   #observer객체를 만듦

    def run(self):
        event_handler = Handler()
        train_handler = TrainHandler()
        self.observer.schedule(event_handler, self.watchDir, recursive=True)
        self.observer.schedule(train_handler, self.trainDir, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Error")
            self.observer.join()


class Handler(FileSystemEventHandler):
    global TRAIN, TEST
#FileSystemEventHandler 클래스를 상속받음.
#아래 핸들러들을 오버라이드 함

    #파일, 디렉터리가 move 되거나 rename 되면 실행
    def on_moved(self, event):
        print(event)

    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        # print(event)
        # test = str(event)
        # print(test[39:-1])
        # file = test[39:-1]
        # A_yyyymmddhhmmss.REQ
        TEST = True
        file_list = comp()
        #
        # for file in file_list:
        # if not TRAIN:
        #     subprocess.call(['python', 'test_main.py', file])
        # else:
        #     print("on train")

        with open("log_test.txt", 'a', encoding='utf-8') as w_file:
            # 시간  포멧 설정%Y= 4자리 연도, %y = 2자리 연도, m=month, d=day, H=24기준 시간, M=분, S=초
            now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            w_file.write(str(now_time))
            w_file.write(' test_log ')
	    # 이벤트 기록
            w_file.write(str(event))
            w_file.write('\n')
            if not TRAIN and TEST:
                for file in file_list:
                # Popen - 별도 터미널에서 작동[]= 콘솔명령어, stdout=output
                    process = subprocess.Popen(['python', '/home/cent/Documents/github/T-friend/main.py','dev', file, 'test'], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                    output, error = process.communicate()
                    print(output.decode('utf-8'))
                #   subprocess.call(['python', 'test_main.py', file])
                    w_file.write("output:")
                    w_file.write(str(output.decode('utf-8')))
                    w_file.write("\n")
                    print("@@procces end@@")
                # w_file.write("error:")
                # w_file.write(str(error))
                # w_file.write('\n')
                    TEST = False
            else:
                print("on train")
            w_file.close()
        # #print('file_list:', file_list)
        #subprocess.call(['python', 'C:\\git\\T-Friend\\main.py'])
        #print(event)

    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)

    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print(event)


class TrainHandler(FileSystemEventHandler):
    global TRAIN, TEST
#FileSystemEventHandler 클래스를 상속받음.
#아래 핸들러들을 오버라이드 함

    #파일, 디렉터리가 move 되거나 rename 되면 실행
    def on_moved(self, event):
        print(event)

    def on_created(self, event): #파일, 디렉터리가 생성되면 실행
        # print(event)
        test = str(event)
        # # print(test[39:-1])
        st = len(test)-22
        en = len(test)-2
        mid = len(test)-5
        if str(test[mid:en])!='REQ' : 
            print("isn't REQ file")
            return
        file = test[st:en]
        # A_yyyymmddhhmmss.REQ

        # file_list = comp()
        #
        # for file in file_list:
        TRAIN = True
        # if TRAIN:
        #     subprocess.call(['python', 'test_long.py'])
        #     TRAIN = False
        # else:
        #     print("error")

        with open("log_test.txt", 'a', encoding='utf-8') as w_file:
            now_time = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
            w_file.write(str(now_time))
            w_file.write(' train log ')
            w_file.write(str(event))
            w_file.write('\n')
            if TRAIN and not TEST:
                process = subprocess.Popen(['python', '/home/cent/Documents/github/T-friend/main.py','dev', file, 'train'], stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
                output, error = process.communicate()
                print(output.decode('utf-8'))
                #   subprocess.call(['python', 'test_main.py', file])
                w_file.write("output:")
                w_file.write(str(output.decode('utf-8')))
                w_file.write("\n")
                print("@@procces end@@")
                #subprocess.call(['python', 'test_long.py'])
                TRAIN = False
            else:
                print("error")
            w_file.close()
        # #print('file_list:', file_list)
        #subprocess.call(['python', 'C:\\git\\T-Friend\\main.py'])
        #print(event)

    def on_deleted(self, event): #파일, 디렉터리가 삭제되면 실행
        print(event)

    def on_modified(self, event): #파일, 디렉터리가 수정되면 실행
        print(event)


if __name__ == '__main__': #본 파일에서 실행될 때만 실행되도록 함
    w = Target()
    w.run()
