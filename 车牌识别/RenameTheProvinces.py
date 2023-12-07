# rename the province
import os
import glob

folder_path = '../pic'
file_list = glob.glob(os.path.join(folder_path, '*.png'))
provinces = ['皖', '闽', '甘', '粤', '桂', '黔', '琼', '冀', '豫', '黑', '鄂', '湘', '吉', '苏', '赣', '辽', '蒙', '宁',
             '青', '鲁', '晋', '陕', '沪', '川', '台', '津', '藏', '新', '滇', '浙']

folder_path = '../pic'
file_list = glob.glob(os.path.join(folder_path, '*.png'))
n = 1

for j in range(30):
    name = '0' + str(n)
    n += 1
    new_file_name = f'{provinces[j]}.png'
    path = 'pic' + '/' + name + '.png'
    os.rename(path, os.path.join(folder_path, new_file_name))
