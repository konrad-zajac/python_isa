import os
import shutil

DIRNAME = '/home/wrutka'
#
# os.path.sep = ';'
# new_dir = os.path.join(DIRNAME, 'Documents')
#
# print(new_dir)
# print(os.getcwd())
#
# dir_to_create = os.path.join(os.getcwd(), 'virus')
# os.mkdir(dir_to_create)
# file_to_create = os.path.join(dir_to_create, 'mojmojmoj')
file_to_create = os.path.join('virus', 'nienieniemojmojmoj')
abs_path = os.path.abspath(file_to_create)
print('abs path: ', abs_path)

print(os.path.join('jakis', 'wyimaginowany', 'pliczek', 'bez', 'pokrycia'))

file_to_move = os.path.join('virus', 'mojmojmoj')
# shutil.move(file_to_create, file_to_move)
print('base name:', os.path.basename(abs_path))

open(os.path.join('virus', 'mojmojmoj'), 'a').close()
os.unlink(os.path.join('virus', 'mojmojmoj'))

print(os.listdir('./'))

shutil.copy('virus/nienieniemojmojmo', 'virus/normalnanazwa')
shutil.copytree()

for actual, sub_dirs, sub_files in os.walk('./'):
    print('jestesmy w catalogu:', actual)
    print('posiada on podkatalogi:', sub_dirs)
    print('posiada on pliki', sub_files)
    print('===========\n')

# os.chdir(new_dir)
#
# print(os.getcwd())
