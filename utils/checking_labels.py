import os
import shutil

def checking_labels(dir_name):
    path_frame = dir_name
    path_labels ='../detection_results/detection_labels'
    path_image = '../dataset_olive/images'
    path_new_labels = '../dataset_olive/labels' 


    try:
        if not os.path.exists(path_image):
            os.makedirs(path_image)
    except OSError:
        print("Errore nella creazione della cartella")
        exit()

    try:
        if not os.path.exists(path_new_labels):
            os.makedirs(path_new_labels)
    except OSError:
        print("Errore nella creazione della cartella")
        exit()


    lista_frames = os.listdir(path_frame)
    lista_labels = os.listdir(path_labels)


    num= 1


    for frames in lista_frames:
        print(frames)
        name = frames.split('.')[0]
        print(name)
        file_txt = name+'.txt'
        print(file_txt)


        for labels in lista_labels:
            if labels == file_txt:
                source_img = path_frame+'/'+frames
                print(source_img)
                destination_img = path_image+'/'+'frame_'+str(num).zfill(4)+'.jpg'
                print(destination_img)
                shutil.copyfile(source_img,destination_img)

                source_txt = path_labels+'/'+labels
                print(source_txt)
                destination_txt = path_new_labels+'/'+'frame_'+str(num).zfill(4)+'.txt'
                print(destination_img)
                shutil.copyfile(source_txt,destination_txt)
               
                num +=1

                

if __name__ == '__main__':  
    checking_labels('../dataset_video/frame_video/frame_video1')


