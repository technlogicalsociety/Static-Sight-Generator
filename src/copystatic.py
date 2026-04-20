import os
import shutil

def static_copy(source, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    for item in os.listdir(source):
        source_path = os.path.join(source, item)
        dest_path = os.path.join(destination, item)

        if os.path.isfile(source_path):
            shutil.copy(source_path, dest_path)
        else:
            static_copy(source_path, dest_path)
