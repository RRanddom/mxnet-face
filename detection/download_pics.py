import os
import urllib

## categories without human face
## abstract animals cats city nature food transport
## technics

image_width = "244"
image_height = "244"
image_bitch_size = 1000
image_base_url = "http://lorempixel.com/"
image_categories = ["business","sports","fashion","people"]
# image_categories = ["abstract","animals","cats","city","nature","food","transport","technics"]

def start_download(total_count = 100):
    for idx in range(0, total_count):
        category_size = len(image_categories)
        dest_url = image_base_url + image_width + '/' + image_height + '/' + image_categories[idx % category_size] + '/'
        #print dest_url
        if(idx % 100 == 0):
            print "index="+str(idx)
        urllib.urlretrieve(dest_url,"test/" + str(idx))

start_download()


#  neg_img = [0 for n in xrange(len(neg_file_list))]
#     for file in neg_file_list:
#         img = Image.open(etc.neg_dir + file)
#         if len(np.shape(np.asarray(img))) != 3:
#             continue
#         neg_img[nid] = img
#         print nid+1, "/" , len(neg_file_list), "th neg image cropping..."
#         neg_db_line = np.zeros((etc.neg_per_img,etc.dim_12), np.float32)
#         for neg_iter in xrange(etc.neg_per_img):

